# The corrupted satellite data feed

satellite_feed = [
    "72-69-76-76-79",
    "87-79-82-76-68",
    42,
    "  _sYstEm_oNlInE_  ",
    "0"
]


def decode_message(encrypted_text):
    codes = encrypted_text.split("-")
    decoded_word = ""

    for code in codes:
        decoded_word = decoded_word + chr(int(code))

    return decoded_word


# Decode the first two satellite messages

word1 = decode_message(satellite_feed[0])
word2 = decode_message(satellite_feed[1])

print("Decoded Word 1: " + word1)
print("Decoded Word 2: " + word2)


# Clean the system status

status = satellite_feed[3]

status = status.strip()
status = status.replace("_", " ")
status = status.strip()
status = status.lower()

print("Cleaned Status: " + status)


# Handle corrupted non-string data

try:
    decode_message(satellite_feed[2])

except AttributeError:
    print("[SYSTEM WARNING]: Skipped corrupted non-string data.")


# Handle the zero battery override

try:
    result = 100 / int(satellite_feed[4])

except ZeroDivisionError:
    print("[SYSTEM WARNING]: Cannot divide by zero override.")