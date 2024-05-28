{ pkgs ? import ./nixpkgs.nix { } }:

with pkgs;

mkShell {
  buildInputs = [
    git
    heroku
    python312
    nixpkgs-fmt
  ];
}
