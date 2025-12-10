# File: lib/diary.py

class Diary:
    def __init__(self):
        self._list_of_entries = []

    def add(self, entry):
        self.entry = entry
        self._list_of_entries.append(self.entry)

    def all(self):
        return [self.entry.title for self.entry in self._list_of_entries]


    def count_words(self):
        return sum(self.entry.count_words() for self.entry in self._list_of_entries)


    def reading_time(self, wpm):
        self.wpm = wpm
        return int(sum(self.entry.reading_time(self.wpm) for self.entry in self._list_of_entries))

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        
        create dictionary so that key:value is time: title and contents from list of diary entry objects
        for each entry in dict, sum the words in both the key and the value to get total words
        total words / wpm = minutes per entry


        pass


