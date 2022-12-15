def sentence_separator(file_path):
    all_sentences = []
    with open(file_path, encoding='utf-8') as f:
        line = f.readline()
        saved_line = None
        while line:
            start = 0
            stop = None
            cntn = 0
            for i in range(len(line)):
                if cntn:
                    cntn - 1
                    continue
                match line[i]:
                    case '.':
                        if i + 2 < len(line) and line[i+1] == '.':
                            stop = i + 2
                            cntn = 2
                        else:
                            stop = i
                    case '!' | '?':
                        stop = i
                if stop:
                    if saved_line:
                        all_sentences.append(saved_line + line[start:stop+1])
                        saved_line = None
                    else: 
                        all_sentences.append(line[start:stop+1])
                    start = stop + 2
                    stop = None

            if line[-2] not in '.!?':
                    if line[-2] == '-':
                        saved_line = saved_line + line[start:-1] if saved_line else line[start:-2]
                    else:
                        saved_line = saved_line + line[start:-1] + ' ' if saved_line else line[start:-1] + ' '
            if line[-1] == '\n':
                line = f.readline()  
            else:
                line = None
        return all_sentences


if __name__ == '__main__':
    for i in sentences('check.txt'):
        print(i)
        