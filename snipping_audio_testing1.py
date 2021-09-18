import os
from pydub import AudioSegment

def audio_snipped(file,start,end):   

    # Opening file and extracting segment
    song = AudioSegment.from_mp3(file)
    extract = song[startTime:endTime]

    # Saving
    file_name = os.path.split(files_path)[1]
    extract.export("clipped_"+file_name, format="mp3")



##############CODE RUNNER########################

files_path = r'C:\Users\Radhika\Desktop\RADZ\RADZ Projects\humit.app\plugin\testing-python\Jimmie Davis - You Are My Sunshine (1940)..mp3'

startMin = 0
startSec = 30

endMin = 1
endSec = 0

startTime = startMin*60*1000+startSec*1000
endTime = endMin*60*1000+endSec*1000

audio_snipped(files_path,startTime,endTime)
