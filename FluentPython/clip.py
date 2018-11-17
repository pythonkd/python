def clip(text, max_len=80):
#     print(len(text))
    '''在max_len前面或者后面第一个出现的空格处截断文本'''
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
#         print(space_before)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(" ", max_len)

            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()