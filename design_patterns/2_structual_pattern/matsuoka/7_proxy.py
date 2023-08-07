# 承認者 → approver
# 部長 → Director
# 課長 → SectionChief
# としました。

from time import sleep


def main():
    sectionchief = SectionChief()

    print(sectionchief.approve_100yen())  # => OK
    print(sectionchief.approve_3000yen())  # => OK


# Subject
class Approver:
    def approve_100yen(self):
        raise NotImplementedError("abstract method")

    def approve_3000yen(self):
        raise NotImplementedError("abstract method")


# Real subject（主体者）
class Director(Approver):
    def approve_100yen(self):
        sleep(10)
        return "OK"

    def approve_3000yen(self):
        sleep(10)
        return "OK"


# Proxy
class SectionChief(Approver):
    def approve_100yen(self):
        return "OK"

    # Directorの処理をラップ. Proxy = Interfaceとして理解。
    # ただしInterfaceと異なるのは、権限など気にする場合はクラスを明示的に分けて実装した方が
    # バグを減らせる
    def approve_3000yen(self):
        return Director().approve_3000yen()


if __name__ == "__main__":
    main()
