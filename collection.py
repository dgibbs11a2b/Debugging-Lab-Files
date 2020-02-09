# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}
for authors, date in authors.items():
    print (authors,"died in", date)

#Correected spelling of authors on line 12
#Removed module "%s", %s and standalone % on line 19
#Corrected the capital D to a lower case d on line 19
#Moved the closed curly bracket from line 20 to line 17
#Added parenthesis around "authors,"died in", date"
