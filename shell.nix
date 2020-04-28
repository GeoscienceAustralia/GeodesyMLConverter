let
  defaultPkgs = import <nixpkgs> {};
  pinnedPkgs = import (defaultPkgs.fetchFromGitHub {
    owner = "NixOS";
    repo = "nixpkgs-channels";
    rev = "3a763b91963"; # 11 July 2017
    sha256 = "0q47hjl01wylp6cdb52fyjbbx45djnz7bwfyj2mfv2lh04iph3s8";
  }) {};

in

{ nixpkgs ? pinnedPkgs }:

let
  pkgs = if nixpkgs == null then defaultPkgs else pinnedPkgs;
  devEnv = with pkgs; buildEnv {
    name = "devEnv";
    paths = [
      python2Packages.virtualenv
      terraform_0_10
      wget
    ];
  };
in
  pkgs.runCommand "setupEnv" {
    buildInputs = [
      devEnv
    ];
    shellHook = ''
      unset SOURCE_DATE_EPOCH
      if [ -e "p2" ]; then
        . p2/bin/activate
      fi

      if [ -e "./aws/aws-env.sh" ]; then
        . ./aws/aws-env.sh
      fi
    '';
  } ""
