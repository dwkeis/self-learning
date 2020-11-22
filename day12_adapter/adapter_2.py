"""my own kind of adapter format"""
class Original:
    def request(self):
        return "the Original one."

class Complex:
    def special_request(self):
        return "eno trever"

class Adapter(Original,Complex):
    def request(self):
        return f"translated : {self.special_request()[::-1]}"

def Output(target="Original"):
    print(target.request())

if __name__ == "__main__":
    original = Original()
    Output(original)
    wrong = Complex()
    print(wrong.special_request())
    adapter = Adapter()
    Output(adapter)
