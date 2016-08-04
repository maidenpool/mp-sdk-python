from tests.test_cases.recombee_test import RecombeeTest
from recombee_api_client.api_requests import *

class BatchTestCase(RecombeeTest):

  def test_batch(self):
    reqs = [
          ResetDatabase(),
          AddItemProperty('num', 'int'),
          AddItemProperty('time', 'timestamp'),
          SetItemValues('item1', {
                          'num': 99,
                          '!cascadeCreate': True}),
          AddItem('item1'),
          SetItemValues('item2', {
                          'num': 68,
                          'time': 27,
                          '!cascadeCreate': True}),
          ListItems(),
          ListItems({'filter': "'num' < 99"}),
          DeleteItem('item1'),
          ListItems({'filter': "'num' >= 99"}),
          AddCartAddition('user', 'item2',  {'timestamp': '2013-10-29T09:38:41.341Z'}),
          AddCartAddition('user', 'item2', {'cascadeCreate': True}),
          ItemBasedRecommendation('item2', 30),
          UserBasedRecommendation('user_id', 25, {'filter': "'num'==68",
                                    'allowNonexistent': True})
    ]

    resp = self.client.send(Batch(reqs))

    codes = [r['code'] for r in resp]
    self.assertEqual(codes, [200, 201, 201, 200, 409, 200, 200, 200, 200, 200, 404, 200, 200, 200])
    self.assertEqual(sorted(resp[6]['json']), ['item1', 'item2'])
    self.assertEqual(resp[7]['json'], ['item2'])
    self.assertEqual(resp[9]['json'], [])
    self.assertEqual(resp[13]['json'], ['item2'])