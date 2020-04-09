class DataLoader:

    def readData(self, loadSonFile):
        with open(loadSonFile, "r") as f:
            data = f.read()

        return data

    def loadSonText(self, data):

        string = ""
        stringOnly = False
        objectStack = [{}]
        waiting = False

        # ------------------------------------------------------------
        # checker = False

        for i in range(len(data)):

            letter = data[i]

            # --------------------------------------------------------
            # if letter == "#":
            #     checker = True

            if letter == '"' and not stringOnly:
                stringOnly = '"'
                continue
            elif letter == '"' and stringOnly == '"':
                stringOnly = False
                continue
            if letter == "'" and not stringOnly:
                stringOnly = "'"
                continue
            elif letter == "'" and stringOnly == "'":
                stringOnly = False
                continue

            if stringOnly:
                string += letter
                # if checker:
                #     print([string], " ---")

            elif waiting and letter != "}":
                string += letter

            elif waiting and letter == "}":
                objectStack[-1][key] = string.strip()
                string = ""
                waiting = False

            else:
                if letter == '{':
                    dataType = self.findDataType(data[i:])

                    if dataType == type(""):
                        waiting = True
                        key = string.strip()
                        string = ""

                    elif dataType == type([]):
                        new_object = []
                        if type(objectStack[-1]) == type([]):
                            objectStack[-1].append(new_object)
                        else:
                            objectStack[-1][string.strip()] = new_object
                        objectStack.append(new_object)
                        string = ""

                    elif dataType == type({}):
                        # Change me to make me better
                        new_object = {}
                        if type(objectStack[-1]) == type([]):
                            objectStack[-1].append(new_object)
                        else:
                            objectStack[-1][string.strip()] = new_object

                        objectStack.append(new_object)
                        string = ""

                elif letter == "}":
                    if type(objectStack[-1]) == type([]):
                        try:
                            string.strip()[-1]
                        except IndexError:
                            pass
                        else:
                            if string.strip()[-1] in ("}", "]", ""):
                                pass
                            else:
                                objectStack[-1].append(string.strip())
                            string = ""

                    objectStack.pop()

                elif letter == ",":
                    try:
                        string[-1]
                    except IndexError:
                        pass
                    else:
                        if string.strip()[-1] in ("}", "]", ""):
                            pass
                        else:
                            objectStack[-1].append(string.strip())
                        string = ""

                else:
                    string += letter

        return objectStack[0]

    def loadSonFile(self, loadFile):
        return self.loadSonText(self.readData(loadFile))

    def findDataType(self, text):
        if text[0] != "{":
            print("Error in param type passed for findDataType")
            raise TypeError

        text = text[1:]

        new_text = ""

        stringCheck = False
        openedBraces = 0
        valueCheck = True

        for letter in text:
            if letter in ("'", '"'):
                if stringCheck:
                    stringCheck = False
                    continue
                else:
                    stringCheck = letter

            if letter == "{" and not stringCheck:
                openedBraces += 1
                valueCheck = False

            elif letter == "}" and not stringCheck:
                if openedBraces:
                    # This was something opened inside the text
                    openedBraces -= 1
                else:
                    # this means that its the original data
                    # which is closing
                    break

                continue

            if (not stringCheck) and (not openedBraces):
                new_text += letter

        if "," in new_text:
            return type([])

        elif valueCheck:
            return type("")

        else:
            return type({})


if __name__ == '__main__':
    try:
        from pprint import pprint as pp
    except ImportError:
        pp = print

    dataLoader = DataLoader()
    pp(dataLoader.loadSonFile("testfile.txt"))
