#!/bin/bash

pdm install

if [  ! -f ".env" ]; then
   cp .env.example .env
fi

tail -f /dev/null