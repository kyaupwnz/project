from pytest_project.set_ import set_
def test_set_():
  coll = {"a": {"b": {"c": 3}}}
  set_(coll, ["a", "b", "c"], 4)
  assert coll["a"]["b"]["c"] == 4

  coll = {"a": {"b": {"c": 3}}} 
  set_(coll, ['x', 'y', 'z'], 5)
  assert coll['x']['y']['z'] == 5
