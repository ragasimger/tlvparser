from itertools import islice

main_data = {
  '''
  Place your dictionary here in which key that 
  you want to place the decoded value from TLV 
  payload.
  '''
  '''
  Eg.:
  "01" : "Data type"
  
  -> Value will be placed in "Data type" key
  -> "01" is the defined key in tlv payload 
  '''
}
## Tag Length Value(TLV) Parser ##
payload_decoded_data = {}
def return_value(ke, dict_data):
    '''
    Return value for the 
    specific key.
    '''
    try:
        x = dict_data[ke]
    except:
        x = None
    return x
def tlv_data_parser(payload, length_len, tag_len, dict_data):
    it = iter(payload)
    while key := "".join(islice(it, tag_len)):
        try:
            length_to_parse = int("".join(islice(it, length_len)))
            value = "".join(islice(it, length_to_parse))
            key = return_value(key, dict_data)
            if key == None:
                return None
            payload_decoded_data[key] = value
        except:
            return None
# Place the dict data to decode
payload_to_decode = {}
# decoded_data = tlv_data_parser(payload_to_decode,{tag to be identified},{length to iter},main_data)
decoded_data = tlv_data_parser(payload_to_decode,2,2,main_data)