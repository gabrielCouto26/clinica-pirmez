import pandas as pd
import unittest
from src.domain.transformer import Transformer


class TestTransformer(unittest.TestCase):
    def test_calculate_share(self):
        """
        Test that it can calculate each medic's share
        when input is medic's procedures and values.
        """
        input = pd.read_csv('tests/fixtures/transformer-input.csv')
        output = pd.read_csv('tests/fixtures/transformer-output.csv')

        result = Transformer().calculate_share(input)

        self.assertIsInstance(
            result, pd.DataFrame, 'Result is not a DataFrame')
        self.assertTrue(result.equals(output), 'Result is incorrect')


if __name__ == '__main__':
    unittest.main()
