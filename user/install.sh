#!/bin/sh -xe

echo --- Copy launch agent plist
mkdir ~/Library/LaunchAgents/ || true
cp -f music-exp.plist ~/Library/LaunchAgents/

echo --- Load launch agent
launchctl load ~/Library/LaunchAgents/music-exp.plist
echo --- INSTALL SUCCESS
