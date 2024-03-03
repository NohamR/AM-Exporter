tell application "Music"
    if it is running then
        if player state is playing then
            set pState to player state
            set pPosition to player position
            set cTrack to current track

            set trackInfo to "{\"status\": \"playing\", \"persistent ID\": \"" & persistent ID of cTrack & "\", \"name\": \"" & name of cTrack & "\", \"time\": \"" & time of cTrack & "\", \"duration\": \"" & duration of cTrack & "\", \"artist\": \"" & artist of cTrack & "\", \"album artist\": \"" & album artist of cTrack & "\", \"composer\": \"" & composer of cTrack & "\", \"album\": \"" & album of cTrack & "\", \"genre\": \"" & genre of cTrack & "\", \"played count\": \"" & played count of cTrack & "\", \"pState\": \"" & pState & "\", \"pPosition\": \"" & pPosition & "\" }"
            return trackInfo
        else
            return "{\"status\": \"not playing\"}"
        end if
    else
        return "{\"status\": \"not running\"}"
    end if
end tell