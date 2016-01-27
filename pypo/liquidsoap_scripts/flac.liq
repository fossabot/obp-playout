            if not icecast_vorbis_metadata then
                source := add(normalize=false, [amplify(0.00001, noise()), !source])
            end

            if stereo then
                ignore(output_stereo(%ogg(%flac(samplerate=44100, channels=2,compression=0, bits_per_sample=16)), !source))
            else
                ignore(output_mono(%ogg(%flac(samplerate=44100, channels=1,compression=0, bits_per_sample=16)), mean(!source)))
            end