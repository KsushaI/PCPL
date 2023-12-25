from operator import itemgetter


class Comp:
    def __init__(self, id, model):
        self.id = id
        self.model = model


class Browser:
    def __init__(self, id, name, visits, comp_id, ):
        self.id = id
        self.name = name
        self.visits = visits
        self.comp_id = comp_id


class Comp_Browser:
    def __init__(self, comp_id, browser_id):
        self.comp_id = comp_id
        self.browser_id = browser_id


# Computers

computers = [
    Comp(1, "Dell XPS 8960"),
    Comp(2, "Latitude 5440"),
    Comp(3, "Alienware Aurora R16"),
    Comp(4, "Latitude 8434"),
    Comp(5, "Latitude 9050"),
    Comp(6, "Origin Millennium 5000D")
]

# Browsers

browsers = [
    Browser(1, "Chrome", 700, 2),
    Browser(2, "Microsoft Edge", 600, 3),
    Browser(3, "Internet Explorer", 200, 4),
    Browser(4, "Avast Secure Browser", 350, 5),
    Browser(5, "Firefox", 550, 1),
    Browser(6, "Vivaldi", 620, 6),
    Browser(7, "Brave", 590, 2),
    Browser(8, "Opera", 330, 4),
    Browser(9, "Yandex Browser", 600, 3),
    Browser(10, "Apple Safari", 400, 5)
]

browsers_comps = [
    Comp_Browser(1, 3),
    Comp_Browser(2, 4),
    Comp_Browser(3, 6),
    Comp_Browser(5, 2),
    Comp_Browser(2, 7),
    Comp_Browser(6, 8),
    Comp_Browser(1, 10),
    Comp_Browser(3, 2),
    Comp_Browser(4, 7),
    Comp_Browser(5, 5),
    Comp_Browser(4, 2),
    Comp_Browser(6, 3)
]


def main():
    # Соединение данных один-ко-многим
    one_to_many = [(b.name, b.visits, c.model)
                   for c in computers
                   for b in browsers
                   if b.comp_id == c.id]
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.model, cb.comp_id, cb.browser_id)
                         for c in computers
                         for cb in browsers_comps
                         if c.id == cb.comp_id]

    many_to_many = [(b.name, comp_model)
                    for comp_model, comp_id, browser_id in many_to_many_temp
                    for b in browsers if b.id == browser_id]

    print('Задание Е1')
    print(*list(filter(lambda i: i[2].find('Latitude') != -1, one_to_many)), end='\n\n')

    print('Задание Е2')
    res_unsorted = []

    for c in computers:
        comp_browsers = list(filter(lambda i: i[2] == c.model, one_to_many))
        if len(comp_browsers) > 0:
            c_visits = [visits for _, visits, _ in comp_browsers]
            c_visits_sum = round(sum(c_visits) / len(comp_browsers), 2)
            res_unsorted.append((c.model, c_visits_sum))

    res = sorted(res_unsorted, key=itemgetter(1), reverse=True)
    print(res, end='\n\n')

    print('Задание Е3')
    print(list(filter(lambda i: i[0].find('A') != -1, many_to_many)))


if __name__ == '__main__':
    main()
