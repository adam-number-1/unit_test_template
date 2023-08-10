import pytest
from unittest.mock import Mock, patch
from typing import Any

# test class for module level functions
# could probably make it one, since the functions differ very little
# but what i dont want is to import stuff, i want to simpy copy
# maybe i can put the functionality outside and just inject it
class TestModule:
    # python -m pytest PATH\FILENAME.py::TestModule::test_FUNCITON

    # SIDE EFFECT VALIDATION
    # this fixture returns a function, that validates side effects
    @pytest.fixture
    def a_validate_side_effect(self) -> bool:
        def validate(tc_key, *args,**kwargs):
            if not tc_key:
                return True
            else:
                raise ValueError('Test case is missing side effect validation')

        return validate

    # SETUP TEARDOWN FIXTURE
    # this sets the and cleans up the tested environment
    @pytest.fixture
    def a_setup_teardown(self):
        def setup_teardown(tc_key, *args,**kwargs):
            if not tc_key:
                yield None
            else:
                raise ValueError('Test case is missing setup-teardown')

        return setup_teardown

    a_test_input_1 = {
        # positional arguments tuple
        'args': (

        ),
        'kwargs': {

        }
    }
    a_expected_output_1 = (

    )
    
    a_side_effect_key_1 = None
    a_setup_teardown_key_1 = None

    @pytest.mark.parametrize(
        "test_input,expected_output,se_key,st_key",
        [
            (
                a_test_input_1, 
                a_expected_output_1,
                a_side_effect_key_1,
                a_setup_teardown_key_1
            )
        ]
    )
    def test_FUNCTION(
        self, 
        test_input, 
        expected_output, 
        se_key,
        st_key,
        a_validate_side_effect,
        a_setup_teardown
    ):
        # setup environment
        st = a_setup_teardown(st_key)
        next(st)

        # get the result
        result = FUNCTION(
            *test_input['args'],
            **test_input['kwargs']
        )
        
        # testing result
        if len(expected_output) == 1:
            assert result == expected_output[0]
        elif len(expected_output) > 1:
            assert result == expected_output
        else:
            raise ValueError('Empty expected output')
        
        # testing the environment changes
        assert a_validate_side_effect(se_key)

        # environment cleanup
        try:
            next(st)
        except StopIteration:
            pass
        else:
            ValueError('unexpected after teardown state')
        

# testing instance methods, instance creations etc
class TestClass:
    # python -m pytest PATH\FILENAME.py::TestModule::test_FUNCITON

    # SIDE EFFECT VALIDATION
    # this fixture returns a function, that validates side effects
    @pytest.fixture
    def a_validate_side_effect(self) -> bool:
        def validate(tc_key, *args,**kwargs):
            if not tc_key:
                return True
            else:
                raise ValueError('Test case is missing side effect validation')

        return validate

    # SETUP TEARDOWN FIXTURE
    # this sets the and cleans up the tested environment
    @pytest.fixture
    def a_setup_teardown(self):
        def setup_teardown(tc_key, *args,**kwargs):
            if not tc_key:
                yield None
            else:
                raise ValueError('Test case is missing setup-teardown')

        return setup_teardown

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
    
    a_side_effect_key_1 = None
    a_setup_teardown_key_1 = None

    # in future i am to remove method below to separate helper module, because
    # i am not looking to change it
    @pytest.mark.parametrize(
        "test_input,expected_output,class_,init,attrs",
        [
            (
                a_test_input_1, 
                a_expected_output_1, 
                a_class_1, 
                a_init_1, 
                a_attrs_1,
                a_side_effect_key_1,
                a_setup_teardown_key_1
            )
        ]
    )
    def test_FUNCTION(
        self, 
        test_input, 
        expected_output, 
        class_, 
        init, 
        attrs,
        se_key,
        st_key,
        a_validate_side_effect,
        a_setup_teardown
    ):
        # setup environment
        st = a_setup_teardown(st_key)
        next(st)

        # initialize tested objects
        obj_ = class_(
            *init['args'],
            **init['kwargs']
        )

        # get the result
        result = obj_.FUNCTION(
            *test_input['args'],
            **test_input['kwargs']
        )
        
        # testing result
        if len(expected_output) == 1:
            assert result == expected_output[0]
        elif len(expected_output) > 1:
            assert result == expected_output
        else:
            raise ValueError('Empty expected output')
        
        # testing attributes of object
        for attr_name, attr_val in attrs.items():
            obj_.__getattribute__(attr_name) == attr_val

        # testing the environment changes
        assert a_validate_side_effect(se_key)

        # environment cleanup
        try:
            next(st)
        except StopIteration:
            pass
        else:
            ValueError('unexpected after teardown state')

