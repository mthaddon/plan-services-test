# plan-services-test

## Description

A charm to illustrate a coverage issue.

## Usage

Running tests for this gives the following:

```
----------------------------------------------------------------------
Ran 1 test in 0.003s

OK
Name           Stmts   Miss  Cover   Missing
--------------------------------------------
src/charm.py      40     11    72%   64-73, 91, 105-109, 113
--------------------------------------------
TOTAL             40     11    72%
```
How is coverage for both code paths of line 88 of `src/charm.py` provided?
That line is:
```
if plan.services != pebble_layer["services"]:
```
But our only test is:
```
    def test_config_changed(self):
        self.harness.update_config({"thing": "foo"})
        self.assertEqual(self.harness.model.unit.status, ActiveStatus())
```
How does this exercise plan.services matching pebble_layer["services"] and the
case when those don't match?

## Developing

Create and activate a virtualenv with the development requirements:

    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements-dev.txt

## Testing

The Python operator framework includes a very nice harness for testing
operator behaviour without full deployment. Just `run_tests`:

    ./run_tests
