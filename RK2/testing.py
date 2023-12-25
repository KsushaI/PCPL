import unittest
from operator import itemgetter
from main import computers, browsers, browsers_comps, main


class TestRK1Functions(unittest.TestCase):
    def test_task_E1(self):
        expected_result = [('Chrome', 700, 'Latitude 5440'), ('Brave', 590, 'Latitude 5440'),
                           ('Internet Explorer', 200, 'Latitude 8434'), ('Opera', 330, 'Latitude 8434'),
                           ('Avast Secure Browser', 350, 'Latitude 9050'), ('Apple Safari', 400, 'Latitude 9050')]
        one_to_many = [(b.name, b.visits, c.model)
                       for c in computers
                       for b in browsers
                       if b.comp_id == c.id]
        filtered_result = list(filter(lambda i: i[2].find('Latitude') != -1, one_to_many))
        self.assertEqual(filtered_result, expected_result)

    def test_task_E2(self):
        expected_result = [('Latitude 5440', 645.0), ('Origin Millennium 5000D', 620.0),
                           ('Alienware Aurora R16', 600.0), ('Dell XPS 8960', 550.0), ('Latitude 9050', 375.0),
                           ('Latitude 8434', 265.0)]
        one_to_many = [(b.name, b.visits, c.model)
                       for c in computers
                       for b in browsers
                       if b.comp_id == c.id]
        res_unsorted = []

        for c in computers:
            comp_browsers = list(filter(lambda i: i[2] == c.model, one_to_many))
            if len(comp_browsers) > 0:
                c_visits = [visits for _, visits, _ in comp_browsers]
                c_visits_sum = round(sum(c_visits) / len(comp_browsers), 2)
                res_unsorted.append((c.model, c_visits_sum))

        res = sorted(res_unsorted, key=itemgetter(1), reverse=True)
        self.assertEqual(res, expected_result)

    def test_task_E3(self):
        expected_result = [('Apple Safari', 'Dell XPS 8960'), ('Avast Secure Browser', 'Latitude 5440')]
        many_to_many_temp = [(c.model, cb.comp_id, cb.browser_id)
                             for c in computers
                             for cb in browsers_comps
                             if c.id == cb.comp_id]

        many_to_many = [(b.name, comp_model)
                        for comp_model, comp_id, browser_id in many_to_many_temp
                        for b in browsers if b.id == browser_id]
        filtered_result = list(filter(lambda i: i[0].find('A') != -1, many_to_many))
        self.assertEqual(filtered_result, expected_result)


if __name__ == '__main__':
    unittest.main()
