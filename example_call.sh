#!/bin/bash

curl http://localhost:5000/ \
  -X POST \
  -H "Content-Type: application/json" \
  -d '[
    {
        "name": "Calculus 1 (Full Length Videos)",
        "is_playlist": "PLF797E961509B4EB5"
    },
    {
        "name":"Calculus 2 (Full Length Videos)",
        "is_playlist": "PLDesaqWTN6EQ2J4vgsN1HyBeRADEh4Cw-"
    },
    {
        "name": "exurb1a",
        "forUsername": "willunicycleforfood"
    }
]'
