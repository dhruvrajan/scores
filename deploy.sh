#!/bin/sh

if [ -z '$1' ]; then
  echo 'Enter the directory to deploy to gh-pages'
  exit 1
fi

git subtree push --prefix $1 origin gh-pages
