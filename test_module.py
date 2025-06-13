import unittest
import sea_level_predictor
import matplotlib as mpl


# Test is for matplotlib 3.2.1 or higher
class SeaLevelPredictorTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        self.assertEqual(actual, expected, "Expected chart title to be 'Rise in Sea Level'")
    
    def test_plot_xlabel(self):
        actual = self.ax.get_xlabel()
        expected = "Year"
        self.assertEqual(actual, expected, "Expected x label to be 'Year'")

    def test_plot_ylabel(self):
        actual = self.ax.get_ylabel()
        expected = "Sea Level (inches)"
        self.assertEqual(actual, expected, "Expected y label to be 'Sea Level (inches)'")

    def test_plot_data_points(self):
        actual = len([collection for collection in self.ax.collections if collection.get_offsets().size > 0])
        expected = 1
        self.assertEqual(actual, expected, "Expected one scatter plot.")
        
    def test_plot_lines(self):
        actual = len(self.ax.lines)
        expected = 2
        self.assertEqual(actual, expected, "Expected two lines on chart.")
        
    def test_plot_line_1(self):
        line_1 = self.ax.lines[0]
        actual_x = line_1.get_xdata()
        actual_y = line_1.get_ydata()
        
        expected_x = [1880.0, 2050.0]
        expected_y = [-0.54, 15.85]
        
        self.assertAlmostEqual(actual_x[0], expected_x[0], places=1, msg="Expected line to start at x=1880")
        self.assertAlmostEqual(actual_x[-1], expected_x[1], places=1, msg="Expected line to end at x=2050")
        self.assertAlmostEqual(actual_y[0], expected_y[0], places=1, msg="Expected line to start at approximately y=-0.54")
        self.assertAlmostEqual(actual_y[-1], expected_y[1], places=1, msg="Expected line to end at approximately y=15.85")

    def test_plot_line_2(self):
        line_2 = self.ax.lines[1]
        actual_x = line_2.get_xdata()
        actual_y = line_2.get_ydata()
        
        expected_x = [2000.0, 2050.0]
        expected_y = [6.95, 14.38]
        
        self.assertAlmostEqual(actual_x[0], expected_x[0], places=1, msg="Expected line to start at x=2000")
        self.assertAlmostEqual(actual_x[-1], expected_x[1], places=1, msg="Expected line to end at x=2050")
        self.assertAlmostEqual(actual_y[0], expected_y[0], places=1, msg="Expected line to start at approximately y=6.95")
        self.assertAlmostEqual(actual_y[-1], expected_y[1], places=1, msg="Expected line to end at approximately y=14.38")

if __name__ == "__main__":
    unittest.main()
