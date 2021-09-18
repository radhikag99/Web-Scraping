import wget
import feedparser
import glob
import os




def get_input(rss_len):
    how_many_downloaded = ""
    
    if rss_len == 0:
        rss_text = "no"
        rss_episodes_text = "episodes"
    elif rss_len == 1:
        rss_text = "is"
        rss_episodes_text = "episode"
    elif rss_len > 1:
        rss_text = "are"
        rss_episodes_text = "episodes"

    
    print("There " + rss_text + " " + str(rss_len) + " " + rss_episodes_text + " in this feed.")
    print("RSS feeds are ordered from most recent entries first, descending order in.")
    print("If an episode exists in the target directory the download will skip that file.")
    print("-------------------------------")
    how_many_downloaded = input("How many recent episodes to download? Enter 0 for them all. - ")
    print("-------------------------------")

    return how_many_downloaded


def validate_input(how_many_num, rss_len):
    
    if (how_many_num.isnumeric()) == True:
        
        if int(how_many_num) < 0 or int(how_many_num) > int(rss_len):
            print("INPUT ERROR - Please Enter A Number Between 0 And " + str(rss_len))
            validated = 0
        else:
            validated = 1
    else:
        print("INPUT ERROR - Please Enter A Number Only.")
        validated = 0

    
    return validated

def Get_Feed(rss_to_load):
    
    print("Getting feed - " + rss_to_load + " please wait...")
    rss_feed_load = feedparser.parse(rss_to_load)
    rss_length = len(rss_feed_load.entries)
    print("Feed loaded.")
    
    
    return rss_feed_load, rss_length

def Download_Files(target_dir, rss_feed, how_many_to_get):
   
    episode_count = 1
    
    os.chdir(target_dir)
    current_files = []
    for file in glob.glob("*.mp3"):
        current_files.append(file)

    
    for episode in rss_feed.entries:

        entry_links = episode.links
        print(entry_links)
        
        mp3_link = entry_links[1]
        mp3_href = mp3_link['href']

        
        temp_mp3_link = mp3_href.split('/')
        print(temp_mp3_link)
        
        temp_mp3_link_last = len(temp_mp3_link) - 1    
        temp_mp3_link = temp_mp3_link[temp_mp3_link_last]

        
        if ".mp3" in temp_mp3_link:
            
            if "?" in temp_mp3_link:
                temp_mp3_link = temp_mp3_link.split("?")
               
                temp_mp3_link = temp_mp3_link[0]

        
        if temp_mp3_link in current_files:
            print("File Exists - SKIPPING DOWNLOAD - " + temp_mp3_link)
        else:
            print("Downloading - " + str(temp_mp3_link))
            wget.download(mp3_link['href'], target_dir)

       
        if int(how_many_to_get) > 0:
            if str(episode_count) == str(how_many_to_get):
                print("--- DOWNLOAD COMPLETE ---")
                break
            else:
                episode_count = episode_count + 1
    
    if int(how_many_to_get) == 0:
        print("--- DOWNLOAD COMPLETE ---")


#---------- Run this through rss feed list----------------
RSS_Target = "http://sellingthecouch.libsyn.com/rss"

# RSS_Target = "https://www.omnycontent.com/d/playlist/aaea4e69-af51-495e-afc9-a9760146922b/8a755b22-8f72-4d44-8ff9-ab79013fda25/6b8a5068-9bea-439f-bd4d-ab79013fda2b/podcast.rss"
local_target_dir = r"C:\Users\Radhika\Desktop\RADZ\RADZ Projects\humit.app\RSS feeds"


RSS_Feed = Get_Feed(RSS_Target)
RSS_Feed_Items = RSS_Feed[0]
RSS_Feed_Count = RSS_Feed[1]

# print(RSS_Feed_Items)
# print(RSS_Feed_Count)
is_valid = 0
while is_valid == 0:
    How_Many = get_input(RSS_Feed_Count)
    is_valid = validate_input(How_Many, RSS_Feed_Count)
else:
    if int(How_Many) == 0:
        File_Count = "All files to - "
    elif int(How_Many) == 1:
        File_Count = str(How_Many) + " file to - "
    else:
        File_Count = str(How_Many) + " files to - "
    print("Downloading " + File_Count + local_target_dir)
    Download_Files(local_target_dir, RSS_Feed_Items, How_Many)

# End 