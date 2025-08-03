#!/bin/bash

# Configuration
DB="AAC"
COLLECTION="animals"
USER="aacuser"
PASS="password"
AUTH_DB="AAC"
CSV_FILE="aac_shelter_outcomes.csv"

# Create user (if needed, when access control is off)
mongosh <<EOF
use $DB
db.createUser({
  user: "$USER",
  pwd: "$PASS",
  roles: [ { role: "readWrite", db: "$DB" } ]
})
EOF

# Import CSV
echo "Importing CSV..."
mongoimport --db $DB \
            --collection $COLLECTION \
            --type csv \
            --file "$CSV_FILE" \
            --headerline \
            --username "$USER" \
            --password "$PASS" \
            --authenticationDatabase "$AUTH_DB"

echo "Done importing $CSV_FILE into $DB.$COLLECTION"