GPG Imagem Viewer

This is a simple image viewer that handles images that were encrypted by GPG.

## Motivation

If you care about the privacy of your pictures/photos, a good way is to encrypt
them. So, even if someone has access to your files, they will need to break your
passphrase AND have access to your GPG Private Key in order to view them.

## Encrypt your files

`gpg --encrypt-files -r <GPG_ID> *.jpg`

More about GPG and how to create your private and public keys: https://www.gnupg.org/gph/en/manual.html

##Dependencies

- PyGTK
- GNUPG: https://www.gnupg.org/
- pip install python-gnupg
- pip install python-magic

## How to run

just do: `./gpg-image_viewer.py <image_file>`

## Running tests

 python -m unittest discover
