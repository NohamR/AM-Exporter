tell application "Music"
    if it is running then
        if player state is playing then
            -- return name of current track & " by " & artist of current track

            -- working :
            -- return raw data of artwork 1 of current track

            -- return properties of sources

            -- return properties of current playlist

            -- set currentPlaylist to container of current track
            -- set currentPlaylistID to persistent ID of currentPlaylist

            -- return properties of currentPlaylist

            -- return properties of current track
                    -- name
                    -- time
                    -- duration
                    -- artist
                    -- album artist
                    -- composer
                    -- album
                    -- genre
                    -- played count

            set pState to player state
            set pPosition to player position

            set cTrack to current track
            -- return raw data of artwork 1 of current track
            -- set trackInfo to "{'''name''': '''" & name of cTrack & "''',
            --     '''time''': '''" & time of cTrack & "''',
            --     '''duration''': '''" & duration of cTrack & "''',
            --     '''artist''': '''" & artist of cTrack & "''',
            --     '''album artist''': '''" & album artist of cTrack & "''',
            --     '''composer''': '''" & composer of cTrack & "''',
            --     '''album''': '''" & album of cTrack & "''',
            --     '''genre''': '''" & genre of cTrack & "''',
            --     '''played count''': '''" & played count of cTrack & "''',
            --     '''pState''' = '''" & pState & "''',
            --     '''pPosition''' = '''" & pPosition & "'''
            --     }"

            -- set trackInfo to "{'''name''': '''" & name of cTrack & "''', '''time''': '''" & time of cTrack & "''', '''duration''': '''" & duration of cTrack & "''', '''artist''': '''" & artist of cTrack & "''', '''album artist''': '''" & album artist of cTrack & "''', '''composer''': '''" & composer of cTrack & "''', '''album''': '''" & album of cTrack & "''', '''genre''': '''" & genre of cTrack & "''', '''played count''': '''" & played count of cTrack & "''' , '''pState''' = '''" & pState & "''', '''pPosition''' = '''" & pPosition & "'''}"

            set trackInfo to "{'''status''': '''playing''', '''name''': '''" & name of cTrack & "''', '''time''': '''" & time of cTrack & "''', '''duration''': '''" & duration of cTrack & "''', '''artist''': '''" & artist of cTrack & "''', '''album artist''': '''" & album artist of cTrack & "''', '''composer''': '''" & composer of cTrack & "''', '''album''': '''" & album of cTrack & "''', '''genre''': '''" & genre of cTrack & "''', '''played count''': '''" & played count of cTrack & "''', '''pState''' : '''" & pState & "''', '''pPosition''' : '''" & pPosition & "''' }"            
            return trackInfo
        else
            return "{'''status''' : '''not playing'''}"
        end if
    else
        return "{'''status''' : '''not running'''}"
    end if
end tell