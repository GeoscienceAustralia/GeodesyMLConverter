#!/usr/bin/env python3

import requests
import logging
import argparse
import io
from pathlib import Path
import time
import datetime
import functools
import re
import configparser

from utils.geodesy_logger import GeodesyLogger

GeodesyLogger.setup()
logger = logging.getLogger('geodesy')


def create_date_time(text_time):
    if text_time is not None and len(text_time) == 20:
        return datetime.datetime.fromisoformat(text_time[0:16])
    else:
        return None


def print_date_time(date_time):
    if date_time is None:
        return "                   "
    else:
        return date_time.strftime("%Y %m %d %H %M %S")


def is_close_date_time(date_time_1, date_time_2):
    if date_time_1 is None and date_time_2 is None:
        return True
    elif date_time_1 is None:
        return False
    elif date_time_2 is None:
        return False
    else:
        delta = date_time_1 - date_time_2
        days = delta.days
        if days < 0:
            delta = date_time_2 - date_time_1
            days = delta.days

        if days >= 1:
            return False
        else:
            if delta.seconds >= 120:
                # 120 imply 2 minutes
                return False
            else:
                return True


def sort_by_date_installed(a, b):
    left = create_date_time(a['dateInstalled'])
    right = create_date_time(b['dateInstalled'])
    if left is None and right is None:
        return 0
    elif left is None:
        return 1
    elif right is None:
        return -1
    else:
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0


def sort_by_date_time(a, b):
    left = a['timeStamp']
    right = b['timeStamp']
    if left is None and right is None:
        return 0
    elif left is None:
        return 1
    elif right is None:
        return -1
    else:
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            left_receiver_start = a.get('receiverStart')
            right_receiver_start = b.get('receiverStart')
            if left_receiver_start is not None and right_receiver_start is not None:
                if left_receiver_start < right_receiver_start:
                    return -1
                elif left_receiver_start > right_receiver_start:
                    return 1

            left_antenna_start = a.get('antennaStart')
            right_antenna_start = b.get('antennaStart')
            if left_antenna_start is not None and right_antenna_start is not None:
                if left_antenna_start < right_antenna_start:
                    return -1
                elif left_antenna_start > right_antenna_start:
                    return 1

            return 0


def arguments():
    options = argparse.ArgumentParser(prog='station_file',
                                      description='Generate station file for Berness software')

    options.add_argument('-f', '--config',
                         default='./setup.ini',
                         metavar='./setup.ini',
                         help='Exclude specific stations')

    options.add_argument('-l', '--url',
                         default='https://gws.geodesy.ga.gov.au/siteLogs?format=json',
                         metavar='https://gws.geodesy.ga.gov.au/siteLogs?format=json',
                         help='URL for geodesy site logs')

    options.add_argument('-o', '--output',
                         default='/tmp/bern/dbTemp/STA/AUT.STA',
                         metavar='/tmp/bern/dbTemp/STA/AUT.STA',
                         help='Generated station file')

    options.add_argument('-v', '--verbose',
                         help='verbose',
                         action='store_true')

    options.add_argument('--version', action='version',
                         version='%(prog)s 1.0, Copyright (c) 2019 by Geodesy, Geoscience Australia')

    return options.parse_args()


class StationFile(object):
    exclude = None
    url = None
    path = None

    @classmethod
    def settings(cls, args):
        try:
            parser = configparser.ConfigParser()
            parser.read([args.config])
            stations = parser.get('setup', 'exclude')
            if stations is not None and len(stations) > 0:
                stations = stations.strip()
                stations = stations.replace(" ", "")
                stations = stations.replace("[", "")
                stations = stations.replace("]", "")
                stations = stations.replace("{", "")
                stations = stations.replace("}", "")
                if len(stations) > 0:
                    cls.exclude = stations

        except Exception as e:
            logger.warning("Setup exception: " + e.message)

        cls.url = args.url
        cls.path = args.output

    @classmethod
    def generate(cls):
        site_log_url = cls.url
        try:
            all_site_logs = []
            size = "&size=100"
            page = "&page="
            index = 0
            url = site_log_url + size + page + str(index)
            while url is not None:
                response = requests.get(url)
                results = response.json()
                all_site_logs.extend(results['_embedded']['siteLogs'])
                if results['_links'].get('next') is not None:
                    index += 1
                    url = site_log_url + size + page + str(index)
                else:
                    url = None

            sorted_site_logs = sorted(all_site_logs,
                                      key=lambda site_log: site_log['siteIdentification']['fourCharacterId'])

            output = io.StringIO()

            cls.type001(output, sorted_site_logs)

            cls.type002(output, sorted_site_logs)

            cls.type003(output)

            cls.type004(output)

            cls.type005(output)

            cls.write_to_file(output)

        except requests.exceptions.RequestException as exception:
            logger.error('Request exception: ' + exception)
        except requests.exceptions.HTTPError as error:
            logger.error("Http Error: " + error)
        except requests.exceptions.ConnectionError as error:
            logger.error('Connection error: ' + error)
        except requests.exceptions.Timeout as timeout:
            logger.error("Timeout: " + timeout)
        except Exception as e:
            logger.fatal("Unhandled exception: " + e.message)
        finally:
            output.close()

    @classmethod
    def type001(cls, output, all_site_logs):
        now_string = time.strftime("%e-%b-%y %H:%M", time.gmtime()).upper()

        output.write("GLOB                                                             {0}\n".format(now_string))
        output.write("--------------------------------------------------------------------------------\n\n")
        output.write("TYPE 001: RENAMING OF STATIONS\n")
        output.write("------------------------------\n\n")
        output.write("STATION NAME          FLG          FROM                   ")
        output.write("TO         OLD STATION NAME      REMARK\n")
        output.write("****************      ***  YYYY MM DD HH MM SS  YYYY MM DD HH MM SS  ")
        output.write("********************  ************************\n")

        for site_log in all_site_logs:
            cls.parse_dome(output, site_log)

        output.write("\n\n")

    @classmethod
    def type002(cls, output, all_site_logs):
        output.write("TYPE 002: STATION INFORMATION\n")
        output.write("-----------------------------\n\n")

        output.write("STATION NAME          FLG          FROM                   TO         ")
        output.write("RECEIVER TYPE         RECEIVER SERIAL NBR   REC #   ANTENNA TYPE          ")
        output.write("ANTENNA SERIAL NBR    ANT #    NORTH      EAST      UP      DESCRIPTION             REMARK\n")
        output.write("****************      ***  YYYY MM DD HH MM SS  YYYY MM DD HH MM SS  ")
        output.write("********************  ********************  ******  ********************  ")
        output.write("********************  ******  ***.****  ***.****  ***.****  **********************  ")
        output.write("************************\n")

        for site_log in all_site_logs:
            cls.parse_log(output, site_log)

        output.write("\n\n")

    @classmethod
    def type003(cls, output):
        output.write("TYPE 003: HANDLING OF STATION PROBLEMS\n")
        output.write("--------------------------------------\n\n")
        output.write("STATION NAME          FLG          FROM                   TO         REMARK\n")
        output.write("****************      ***  YYYY MM DD HH MM SS  YYYY MM DD HH MM SS  ")
        output.write("************************\n")
        output.write("\n\n")

    @classmethod
    def type004(cls, output):
        output.write("TYPE 004: STATION COORDINATES AND VELOCITIES (ADDNEQ)\n")
        output.write("-----------------------------------------------------\n")
        output.write("                                        RELATIVE CONSTR. POSITION     ")
        output.write("RELATIVE CONSTR. VELOCITY\n")
        output.write("STATION NAME 1        STATION NAME 2        NORTH     EAST      UP        ")
        output.write("NORTH     EAST      UP\n")
        output.write("****************      ****************      ")
        output.write("**.*****  **.*****  **.*****  **.*****  **.*****  **.*****\n")
        output.write("\n\n")

    @classmethod
    def type005(cls, output):
        output.write("TYPE 005: HANDLING STATION TYPES\n")
        output.write("--------------------------------\n\n")
        output.write("STATION NAME          FLG  FROM                 TO                   ")
        output.write("MARKER TYPE           REMARK\n")
        output.write("****************      ***  YYYY MM DD HH MM SS  YYYY MM DD HH MM SS  ")
        output.write("********************  ************************\n")
        output.write("\n\n\n\n\n\n")

    @classmethod
    def format_serial_number(cls, text):
        # Get the last 6 digits for unique
        if text is None or not text:
            return "999999"

        serial_number_length_limit = 6
        serial_number = ""
        index = len(text) - 1
        while index >= 0:
            ch = text[index]
            index -= 1
            if ch.isdigit():
                serial_number = ch + serial_number
                if len(serial_number) >= serial_number_length_limit:
                    return serial_number

        if len(serial_number) == 0:
            return "999999"
        else:
            return serial_number

    @classmethod
    def find_close_timestamp(cls, date_time, timestamps):
        for record in timestamps:
            exist_date_time = record['timeStamp']
            if is_close_date_time(date_time, exist_date_time):
                return record
        return None

    @classmethod
    def insert_antenna(cls, antenna, timestamps):
        installed = create_date_time(antenna['dateInstalled'])
        antenna['installed'] = installed

        install_timestamp = dict(antennaStart=1, timeStamp=installed, antenna=antenna)
        timestamps.append(install_timestamp)

        removed = None
        if antenna['dateRemoved'] is not None:
            removed = create_date_time(antenna['dateRemoved'])
            if removed.minute == 59 and removed.hour == 23:
                removed += datetime.timedelta(seconds=60)

        antenna['removed'] = removed

        remove_timestamp = dict(antennaStart=0, timeStamp=removed, antenna=antenna)
        timestamps.append(remove_timestamp)

    @classmethod
    def insert_receiver(cls, receiver, timestamps):
        installed = create_date_time(receiver['dateInstalled'])
        receiver['installed'] = installed

        removed = None
        if receiver['dateRemoved'] is not None:
            removed = create_date_time(receiver['dateRemoved'])
            if removed.minute == 59 and removed.hour == 23:
                removed += datetime.timedelta(seconds=60)

        receiver['removed'] = removed
        record = cls.find_close_timestamp(receiver['installed'], timestamps)
        if record is not None:
            record['receiverStart'] = 1
            record['receiver'] = receiver
        else:
            install_time_stamp = dict(receiverStart=1, timeStamp=receiver['installed'], receiver=receiver)
            timestamps.append(install_time_stamp)

        record = cls.find_close_timestamp(receiver['removed'], timestamps)
        if record is not None:
            record['receiverStart'] = 0
            record['receiver'] = receiver
        else:
            remove_time_stamp = dict(receiverStart=0, timeStamp=receiver['removed'], receiver=receiver)
            timestamps.append(remove_time_stamp)

    @classmethod
    def parse_dome(cls, output, site_log):
        site = site_log['siteIdentification']['fourCharacterId']
        if cls.is_excluded(site):
            return

        gnss_antennas = site_log['gnssAntennas']
        remarks = 'site_log'

        if gnss_antennas is None or not gnss_antennas:
            logger.error("Site: " + site + " have no antennas")
            return

        stamps = []
        for antenna in gnss_antennas:
            cls.insert_antenna(antenna, stamps)

        sorted_stamps = sorted(stamps, key=functools.cmp_to_key(sort_by_date_time))
        date_removed = print_date_time(sorted_stamps[-1]['timeStamp'])

        domes_number = site_log['siteIdentification']['iersDOMESNumber']
        if not domes_number:
            domes_number = "         "
        else:
            domes_number = domes_number.strip()
            if len(domes_number) != 9:
                logger.error(site + ": DOMES number " + domes_number + " seems to be incorrect")

        date_installed = print_date_time(create_date_time(site_log['siteIdentification']['dateInstalled']))
        line = '{:4} {:9}        001  {:19}  {:19}  {:4}*                 {:24}'.format(site,
                                                                                        domes_number,
                                                                                        date_installed,
                                                                                        date_removed,
                                                                                        site,
                                                                                        remarks)
        output.write(line + "\n")

    @classmethod
    def location(cls, site_log):
        description = ""
        description_limit = 22
        if site_log['siteLocation']['state'] is not None:
            state = site_log['siteLocation']['state']

            pattern = re.compile("Northern Territory", re.IGNORECASE)
            state = pattern.sub("NT", state)

            pattern = re.compile("South Australia", re.IGNORECASE)
            state = pattern.sub("SA", state)

            pattern = re.compile("Western Australia", re.IGNORECASE)
            state = pattern.sub("WA", state)

            pattern = re.compile("New South Wales", re.IGNORECASE)
            state = pattern.sub("NSW", state)

            pattern = re.compile("Australian Antarctic Territory \(AAT\)", re.IGNORECASE)
            state = pattern.sub("AAT", state)

            pattern = re.compile("Australian Antarctic Territory", re.IGNORECASE)
            state = pattern.sub("AAT", state)

            pattern = re.compile("Australian Capital Territory \(ACT\)", re.IGNORECASE)
            state = pattern.sub("ACT", state)

            pattern = re.compile("Australian Capital Territory", re.IGNORECASE)
            state = pattern.sub("ACT", state)

            pattern = re.compile("QUEENSLAND", re.IGNORECASE)
            state = pattern.sub("QLD", state)

            pattern = re.compile("Victoria", re.IGNORECASE)
            state = pattern.sub("VIC", state)

            pattern = re.compile("Tasmania", re.IGNORECASE)
            state = pattern.sub("TAS", state)

            state = state.strip()
            if state is not None and len(state) > 0:
                description = state + ", "

        country = site_log['siteLocation']['country']
        if country is not None:
            description += country

        return description[0:description_limit]

    @classmethod
    def parse_log(cls, output, site_log):
        site = site_log['siteIdentification']['fourCharacterId']
        if cls.is_excluded(site):
            return

        remarks = 'site_log'
        description = cls.location(site_log)

        gnss_antennas = site_log['gnssAntennas']
        if gnss_antennas is None or not gnss_antennas:
            logger.error("Site: " + site + " have no antennas")
            return

        gnss_antennas = sorted(gnss_antennas, key=functools.cmp_to_key(sort_by_date_installed))
        timestamps = []
        for antenna in gnss_antennas:
            cls.insert_antenna(antenna, timestamps)

        gnss_receivers = site_log['gnssReceivers']
        if gnss_receivers is None or not gnss_receivers:
            logger.error("Site: " + site + " have no receivers")
            return

        gnss_receivers = sorted(gnss_receivers, key=functools.cmp_to_key(sort_by_date_installed))
        if len(gnss_receivers) == 1:
            cls.insert_receiver(gnss_receivers[0], timestamps)
        else:
            previous_receiver = None
            for receiver in gnss_receivers:
                installed = create_date_time(receiver['dateInstalled'])
                receiver['installed'] = installed

                removed = None
                if receiver['dateRemoved'] is not None:
                    removed = create_date_time(receiver['dateRemoved'])
                    if removed.minute == 59 and removed.hour == 23:
                        removed += datetime.timedelta(seconds=60)
                receiver['removed'] = removed

                receiver['merged'] = 0
                if previous_receiver is not None:
                    if previous_receiver['type'] == receiver['type'] and \
                       previous_receiver['serialNumber'] == receiver['serialNumber'] and \
                       is_close_date_time(installed, previous_receiver['removed']):
                        previous_receiver['removed'] = receiver['removed']
                        receiver['merged'] = 1

                if not receiver['merged']:
                    previous_receiver = receiver

            for receiver in gnss_receivers:
                if receiver['merged']:
                    continue

                record = cls.find_close_timestamp(receiver['installed'], timestamps)
                if record is not None:
                    record['receiverStart'] = 1
                    record['receiver'] = receiver
                else:
                    install_timestamp = dict(receiverStart=1, timeStamp=receiver['installed'], receiver=receiver)
                    timestamps.append(install_timestamp)

                record = cls.find_close_timestamp(receiver['removed'], timestamps)
                if record is not None:
                    record['receiverStart'] = 0
                    record['receiver'] = receiver
                else:
                    remove_timestamp = dict(receiverStart=0, timeStamp=receiver['removed'], receiver=receiver)
                    timestamps.append(remove_timestamp)

        sorted_timestamps = sorted(timestamps, key=functools.cmp_to_key(sort_by_date_time))

        domes_number = site_log['siteIdentification']['iersDOMESNumber']
        if not domes_number:
            domes_number = "         "
        else:
            domes_number = domes_number.strip()
            if len(domes_number) != 9:
                logger.error(site + ": DOMES number " + domes_number + " seems to be incorrect")

        size = len(sorted_timestamps)
        antenna_valid = 0
        receiver_valid = 0

        i = 1
        while i < size:
            previous = sorted_timestamps[i-1]
            current = sorted_timestamps[i]
            advance = None
            if i < size - 2:
                advance = sorted_timestamps[i+1]

            if previous.get('antennaStart') is not None:
                antenna_valid = previous['antennaStart']

            if previous.get('receiverStart') is not None:
                receiver_valid = previous['receiverStart']

            if antenna_valid and receiver_valid:
                start_date = print_date_time(previous['timeStamp'])
                current_timestamp = current['timeStamp']
                if advance is not None and current_timestamp is not None and current_timestamp == advance['timeStamp']:
                    decreased = current_timestamp - datetime.timedelta(seconds=1)
                    end_date = print_date_time(decreased)
                else:
                    end_date = print_date_time(current['timeStamp'])

                previous_receiver = cls.find_previous_receiver(sorted_timestamps, i - 1)
                receiver_type = previous_receiver['type']
                receiver_type = receiver_type.strip()

                previous_antenna = cls.find_previous_antenna(sorted_timestamps, i - 1)
                antenna_type = previous_antenna['type']
                antenna_type = antenna_type.strip()

                pattern = re.compile(r'^(?P<antenna>.+)\s+(?P<radome>\w{4})$')
                extracted_radome_type = None
                ok = re.match(pattern, antenna_type)
                if ok:
                    antenna_type = ok.group('antenna').strip()
                    extracted_radome_type = ok.group('radome')
                else:
                    logger.error(site + ": " + antenna_type + " seems to be incorrect")

                receiver_serial = previous_receiver['serialNumber']
                antenna_serial = previous_antenna['serialNumber']

                receiver_serial_number = cls.format_serial_number(receiver_serial)
                antenna_serial_number = cls.format_serial_number(antenna_serial)

                antenna_radome_type = None
                if previous_antenna['antennaRadomeType'] is None or not previous_antenna['antennaRadomeType']:
                    antenna_radome_type = 'NONE'
                else:
                    antenna_radome_type = previous_antenna['antennaRadomeType']
                    antenna_radome_type = antenna_radome_type.strip()
                if antenna_radome_type != extracted_radome_type:
                    logger.error(site + ": " + antenna_radome_type + " antenna or radome seems to be incorrect")

                antenna_arp_north = '{: 1.4f}'.format(float(previous_antenna['markerArpNorthEcc']))
                antenna_arp_east = '{: 1.4f}'.format(float(previous_antenna['markerArpEastEcc']))
                antenna_arp_up = '{: 1.4f}'.format(float(previous_antenna['markerArpUpEcc']))

                format = '{:4} {:9}        001  {:19}  {:19}  {:20}  {:20}  {:6}  {:15} {:4}  {:20}  {:6}  ' + \
                         ' {:7}   {:7}   {:7}  {:22}  {:24}'
                line = format.format(site, domes_number, start_date, end_date,
                                     receiver_type, receiver_serial, receiver_serial_number,
                                     antenna_type, antenna_radome_type, antenna_serial, antenna_serial_number,
                                     antenna_arp_north, antenna_arp_east, antenna_arp_up,
                                     description, remarks)

                output.write(line + "\n")

            i += 1

        return

    @classmethod
    def find_previous_receiver(cls, timestamps, index):
        i = index
        while i >= 0:
            receiver = timestamps[i].get('receiver')
            if receiver is not None:
                return receiver
            i -= 1

        return None

    @classmethod
    def find_previous_antenna(cls, timestamps, index):
        i = index
        while i >= 0:
            antenna = timestamps[i].get('antenna')
            if antenna is not None:
                return antenna
            i -= 1

        return None

    @classmethod
    def print_record(cls, record):
        antenna_start = record.get('antennaStart')
        if antenna_start is not None:
            logger.debug("Antenna Start = " + str(record.get('antennaStart')) + "\n")

        antenna = record.get('antenna')
        if antenna is not None:
            logger.debug("Antenna type = " + record.get('antenna').get('type') + "\n")

        date_time = record.get('timeStamp')
        if date_time is not None:
            logger.debug("timeStamp = " + print_date_time(date_time) + "\n")
        else:
            logger.debug("timeStamp = None \n")

        receiver_start = record.get('receiverStart')
        if receiver_start is not None:
            logger.debug("Receiver Start = " + str(record.get('receiverStart')) + "\n")

        receiver = record.get('receiver')
        if receiver is not None:
            logger.debug("Receiver type = " + record.get('receiver').get('type') + "\n")

    @classmethod
    def is_excluded(cls, site):
        return cls.exclude is not None and cls.exclude.find(site) >= 0

    @classmethod
    def write_to_file(cls, output):
        try:
            directory = Path(cls.path).parent
            directory.mkdir(parents=True, exist_ok=True)
            full_path = Path(cls.path)
            with full_path.open(mode='w') as station_file:
                station_file.write(output.getvalue())
        except Exception as e:
            logger.error("Write to file failure: " + e.message)


# ==============================================================================
def main():

    StationFile.settings(arguments())
    StationFile.generate()


# ==============================================================================
if __name__ == '__main__':
    main()
