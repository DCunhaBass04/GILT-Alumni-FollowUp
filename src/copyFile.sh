#!/bin/bash

# Nome do remote configurado no rclone
REMOTE_NAME="sharepoint"

# Caminho dentro do SharePoint/Teams
SHAREPOINT_SITE="General/Respostas.xlsx"

DESTINO_LOCAL="$HOME/respostas/Respostas.xlsx"

echo " CHECKING ACCESS..."
rclone ls "$REMOTE_NAME:$SHAREPOINT_SITE" > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo " ERROR: File not found. Check if variables are correctly defined and authenticated."
    exit 1
fi

echo " STARTING DOWNLOAD FROM 'Respostas.xlsx'..."
rclone copy "$REMOTE_NAME:$SHAREPOINT_SITE" "$HOME/respostas/" --progress

if [ $? -eq 0 ]; then
    echo " SUCCESS: File copied to the following location: $DESTINO_LOCAL"
else
    echo " ERROR: Didn't manage to copy the file."
fi