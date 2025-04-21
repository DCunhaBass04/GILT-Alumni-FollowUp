#!/bin/bash

rclone mount "sharepoint:General" ~/TeamsDrive \
  --vfs-cache-mode writes \
  --allow-other