import pytest
from unittest.mock import Mock, patch
from typing import Any

# test class for module level functions
class TestModule:
    # unittest of a side effecting function
    # python -m pytest PATH\FILENAME.py::TestModule::test_FUNCITON
    @pytest.fixture
    def setup_teardown(self):
        # setup
        yield
        # teardown

    a_test_input_1 = {
        # positional arguments tuple
        'args': (

        ),
        'kwargs': {

        }
    }
    a_expected_output_1 = (
        # put none if the side effecting dunction returns nothing
    )
    def a_side_effect_test_1(self, *args, **kwargs) -> bool:
        return True

    @pytest.mark.parametrize(
        "test_input,expected_output,side_effect",
        (a_test_input_1, a_expected_output_1, a_side_effect_test_1)
    )
    def test_FUNCTION(
        self, 
        test_input, 
        expected_output, 
        side_effect, 
        setup_teardown
    ):
        result = FUNCTION(
            *test_input['args'],
            **test_input['kwargs']
        )
        if len(expected_output) == 1:
            assert result == expected_output[0]
        elif len(expected_output) > 1:
            assert result == expected_output
        else:
            raise ValueError('Empty expected output')
        
        assert side_effect()
        
# testing instance methods, instance creations etc
class TestClass:
    # python -m pytest PATH\FILENAME.py::TestModule::test_FUNCITON
    @pytest.fixture
    def setup_teardown(self):
        # setup
        yield
        # teardown
    a_test_input_1 = {
        # positional arguments tuple
        'args': (

        ),
        'kwargs': {

        }
    }
    a_expected_output_1 = (

    )
    a_class_1: Any
    a_init_1 = {
        # positional arguments tuple
        'args': (

        ),
        'kwargs': {

        }   
    }
    a_attrs_1 = {

    }
    def a_side_effect_test_1(self, *args, **kwargs) -> bool:
        return True
    @pytest.mark.parametrize(
        "test_input,expected_output,class_,init,attrs,side_effect_test",
        (a_test_input_1, a_expected_output_1, a_class_1, a_init_1, a_attrs_1, a_side_effect_test_1)
    )
    def test_FUNCTION(self, test_input, expected_output, class_, init, attrs,side_effect_test):
        obj_ = class_(
            *init['args'],
            **init['kwargs']
        )

        result = obj_.FUNCTION(
            *test_input['args'],
            **test_input['kwargs']
        )
        
        if len(expected_output) == 1:
            assert result == expected_output[0]
        elif len(expected_output) > 1:
            assert result == expected_output
        else:
            raise ValueError('Empty expected output')
        
        for attr_name, attr_val in attrs.items():
            obj_.__getattribute__(attr_name) == attr_val

        assert side_effect_test()