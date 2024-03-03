#!/bin/sh -xe
echo --- Unload launch agent
launchctl unload ~/Library/LaunchAgents/music-exp.plist
echo --- Remove launch agent plist
rm -f ~/Library/LaunchAgents/music-exp.plist || true
echo --- UNINSTALL SUCCESS
