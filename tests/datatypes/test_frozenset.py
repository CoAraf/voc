from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class FrozensetTests(TranspileTestCase):
    def test_creation(self):
        # Empty dict
        self.assertCodeExecution("""
            x = frozenset()
            print(x)

            x = frozenset({'a'})
            print(x)

            y = {1,2}
            x = frozenset(y)
            print(x)
            y = {3}
            print(x)

            y = ['c']
            x = frozenset(y)
            print(x)
            y.append('d')
            print(x)

            y = (1,2)
            x = frozenset(y)
            print(x)
            y = ()
            print(x)

            y ='a'
            x = frozenset(y)
            print(x)
            y = y + 'b'
            print(x)

            """)

    def test_contains(self):
        # Normal Contains
        self.assertCodeExecution("""
            x = frozenset()
            print(1 in x)

            x = frozenset({'a'})
            print('a' in x)
            print('b' in x)

            y = {1,2}
            x = frozenset(y)
            print(2 in x)
            print(3 in x)

            y = ['c']
            x = frozenset(y)
            print('c' in x)
            print('a' in x)

            y = (1,2)
            x = frozenset(y)
            print(3 in x)
            print(1 in x)

            y = 'a'
            x = frozenset(y)
            print('e' in x)
            print('a' in x)

            """)

    def test_not_contains(self):
        # Normal Not Contains
        self.assertCodeExecution("""
            x = frozenset()
            print(1 in x)

            x = frozenset({'a'})
            print('b' not in x)
            print('a' not in x)

            y = {1,2}
            x = frozenset(y)
            print(4 not in x)
            print(1 not in x)

            y = ['c']
            x = frozenset(y)
            print('d' not in x)
            print('c' not in x)

            y = (1,2)
            x = frozenset(y)
            print(1 not in x)
            print(3 not in x)

            y = 'a'
            x = frozenset(y)
            print('a' not in x)
            print('d' not in x)

            """)

    def test_iteration(self):
        self.assertCodeExecution("""
            x = {1, 2, 3}
            y = frozenset()
            #We are not printing each element because python and voc store the items in different ways.
            for s in x:
                print(x.__contains__(s))
            for s in y:
                print(y.__conatins__(s))

            """)

    def test_copy(self):
        self.assertCodeExecution("""
            x = frozenset()
            y = x.copy()
            print(x is y)

            x = frozenset({'a'})
            y = x.copy()
            print(x is y)

            y = {1,2}
            x = frozenset(y)
            z = x.copy()
            print(x is z)

            y = ['c']
            x = frozenset(y)
            z = x.copy()
            print(x is z)

            y = (1,2)
            x = frozenset(y)
            z = x.copy()
            print(x is z)

            y = 'a'
            x = frozenset(y)
            z = x.copy()
            print(x is z)

            """)


class UnaryFrozensetOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'frozenset'

    not_implemented = []


class BinaryFrozensetOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'frozenset'

    not_implemented = [
        'test_add_bool',
        'test_add_bytearray',
        'test_add_bytes',
        'test_add_class',
        'test_add_complex',
        'test_add_dict',
        'test_add_float',
        'test_add_frozenset',
        'test_add_int',
        'test_add_list',
        'test_add_None',
        'test_add_NotImplemented',
        'test_add_range',
        'test_add_set',
        'test_add_slice',
        'test_add_str',
        'test_add_tuple',

        'test_and_bool',
        'test_and_bytearray',
        'test_and_bytes',
        'test_and_class',
        'test_and_complex',
        'test_and_dict',
        'test_and_float',
        'test_and_frozenset',
        'test_and_int',
        'test_and_list',
        'test_and_None',
        'test_and_NotImplemented',
        'test_and_range',
        'test_and_set',
        'test_and_slice',
        'test_and_str',
        'test_and_tuple',

        'test_direct_eq_bool',
        'test_direct_eq_bytearray',
        'test_direct_eq_bytes',
        'test_direct_eq_class',
        'test_direct_eq_complex',
        'test_direct_eq_dict',
        'test_direct_eq_float',
        'test_direct_eq_frozenset',
        'test_direct_eq_int',
        'test_direct_eq_list',
        'test_direct_eq_None',
        'test_direct_eq_NotImplemented',
        'test_direct_eq_range',
        'test_direct_eq_set',
        'test_direct_eq_slice',
        'test_direct_eq_str',
        'test_direct_eq_tuple',

        'test_direct_ne_bool',
        'test_direct_ne_bytearray',
        'test_direct_ne_bytes',
        'test_direct_ne_class',
        'test_direct_ne_complex',
        'test_direct_ne_dict',
        'test_direct_ne_float',
        'test_direct_ne_frozenset',
        'test_direct_ne_int',
        'test_direct_ne_list',
        'test_direct_ne_None',
        'test_direct_ne_NotImplemented',
        'test_direct_ne_range',
        'test_direct_ne_set',
        'test_direct_ne_slice',
        'test_direct_ne_str',
        'test_direct_ne_tuple',

        'test_direct_le_bool',
        'test_direct_le_bytearray',
        'test_direct_le_bytes',
        'test_direct_le_class',
        'test_direct_le_complex',
        'test_direct_le_dict',
        'test_direct_le_float',
        'test_direct_le_frozenset',
        'test_direct_le_int',
        'test_direct_le_list',
        'test_direct_le_None',
        'test_direct_le_NotImplemented',
        'test_direct_le_range',
        'test_direct_le_set',
        'test_direct_le_slice',
        'test_direct_le_str',
        'test_direct_le_tuple',

        'test_direct_lt_bool',
        'test_direct_lt_bytearray',
        'test_direct_lt_bytes',
        'test_direct_lt_class',
        'test_direct_lt_complex',
        'test_direct_lt_dict',
        'test_direct_lt_float',
        'test_direct_lt_frozenset',
        'test_direct_lt_int',
        'test_direct_lt_list',
        'test_direct_lt_None',
        'test_direct_lt_NotImplemented',
        'test_direct_lt_range',
        'test_direct_lt_set',
        'test_direct_lt_slice',
        'test_direct_lt_str',
        'test_direct_lt_tuple',

        'test_direct_ge_bool',
        'test_direct_ge_bytearray',
        'test_direct_ge_bytes',
        'test_direct_ge_class',
        'test_direct_ge_complex',
        'test_direct_ge_dict',
        'test_direct_ge_float',
        'test_direct_ge_frozenset',
        'test_direct_ge_int',
        'test_direct_ge_list',
        'test_direct_ge_None',
        'test_direct_ge_NotImplemented',
        'test_direct_ge_range',
        'test_direct_ge_set',
        'test_direct_ge_slice',
        'test_direct_ge_str',
        'test_direct_ge_tuple',

        'test_direct_gt_bool',
        'test_direct_gt_bytearray',
        'test_direct_gt_bytes',
        'test_direct_gt_class',
        'test_direct_gt_complex',
        'test_direct_gt_dict',
        'test_direct_gt_float',
        'test_direct_gt_frozenset',
        'test_direct_gt_int',
        'test_direct_gt_list',
        'test_direct_gt_None',
        'test_direct_gt_NotImplemented',
        'test_direct_gt_range',
        'test_direct_gt_set',
        'test_direct_gt_slice',
        'test_direct_gt_str',
        'test_direct_gt_tuple',

        'test_eq_class',

        'test_floor_divide_bool',
        'test_floor_divide_bytearray',
        'test_floor_divide_bytes',
        'test_floor_divide_class',
        'test_floor_divide_dict',
        'test_floor_divide_float',
        'test_floor_divide_frozenset',
        'test_floor_divide_int',
        'test_floor_divide_list',
        'test_floor_divide_None',
        'test_floor_divide_NotImplemented',
        'test_floor_divide_range',
        'test_floor_divide_set',
        'test_floor_divide_slice',
        'test_floor_divide_str',
        'test_floor_divide_tuple',

        'test_ge_class',

        'test_gt_class',

        'test_le_class',

        'test_lshift_bool',
        'test_lshift_bytearray',
        'test_lshift_bytes',
        'test_lshift_class',
        'test_lshift_complex',
        'test_lshift_dict',
        'test_lshift_float',
        'test_lshift_frozenset',
        'test_lshift_int',
        'test_lshift_list',
        'test_lshift_None',
        'test_lshift_NotImplemented',
        'test_lshift_range',
        'test_lshift_set',
        'test_lshift_slice',
        'test_lshift_str',
        'test_lshift_tuple',

        'test_lt_class',

        'test_modulo_bool',
        'test_modulo_bytearray',
        'test_modulo_bytes',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_range',
        'test_modulo_set',
        'test_modulo_slice',
        'test_modulo_str',
        'test_modulo_tuple',

        'test_multiply_bool',
        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_dict',
        'test_multiply_float',
        'test_multiply_frozenset',
        'test_multiply_int',
        'test_multiply_list',
        'test_multiply_None',
        'test_multiply_NotImplemented',
        'test_multiply_range',
        'test_multiply_set',
        'test_multiply_slice',
        'test_multiply_str',
        'test_multiply_tuple',

        'test_ne_bool',
        'test_ne_bytearray',
        'test_ne_bytes',
        'test_ne_class',
        'test_ne_complex',
        'test_ne_dict',
        'test_ne_float',
        'test_ne_frozenset',
        'test_ne_int',
        'test_ne_list',
        'test_ne_None',
        'test_ne_NotImplemented',
        'test_ne_range',
        'test_ne_set',
        'test_ne_slice',
        'test_ne_str',
        'test_ne_tuple',

        'test_or_bool',
        'test_or_bytearray',
        'test_or_bytes',
        'test_or_class',
        'test_or_complex',
        'test_or_dict',
        'test_or_float',
        'test_or_frozenset',
        'test_or_int',
        'test_or_list',
        'test_or_None',
        'test_or_NotImplemented',
        'test_or_range',
        'test_or_set',
        'test_or_slice',
        'test_or_str',
        'test_or_tuple',

        'test_power_bool',
        'test_power_bytearray',
        'test_power_bytes',
        'test_power_class',
        'test_power_complex',
        'test_power_dict',
        'test_power_float',
        'test_power_frozenset',
        'test_power_int',
        'test_power_list',
        'test_power_None',
        'test_power_NotImplemented',
        'test_power_range',
        'test_power_set',
        'test_power_slice',
        'test_power_str',
        'test_power_tuple',

        'test_rshift_bool',
        'test_rshift_bytearray',
        'test_rshift_bytes',
        'test_rshift_class',
        'test_rshift_complex',
        'test_rshift_dict',
        'test_rshift_float',
        'test_rshift_frozenset',
        'test_rshift_int',
        'test_rshift_list',
        'test_rshift_None',
        'test_rshift_NotImplemented',
        'test_rshift_range',
        'test_rshift_set',
        'test_rshift_slice',
        'test_rshift_str',
        'test_rshift_tuple',

        'test_subscr_bool',
        'test_subscr_bytearray',
        'test_subscr_bytes',
        'test_subscr_class',
        'test_subscr_complex',
        'test_subscr_dict',
        'test_subscr_float',
        'test_subscr_frozenset',
        'test_subscr_int',
        'test_subscr_list',
        'test_subscr_None',
        'test_subscr_NotImplemented',
        'test_subscr_range',
        'test_subscr_set',
        'test_subscr_slice',
        'test_subscr_str',
        'test_subscr_tuple',

        'test_subtract_bool',
        'test_subtract_bytearray',
        'test_subtract_bytes',
        'test_subtract_class',
        'test_subtract_complex',
        'test_subtract_dict',
        'test_subtract_float',
        'test_subtract_frozenset',
        'test_subtract_int',
        'test_subtract_list',
        'test_subtract_None',
        'test_subtract_NotImplemented',
        'test_subtract_range',
        'test_subtract_set',
        'test_subtract_slice',
        'test_subtract_str',
        'test_subtract_tuple',

        'test_true_divide_bool',
        'test_true_divide_bytearray',
        'test_true_divide_bytes',
        'test_true_divide_class',
        'test_true_divide_complex',
        'test_true_divide_dict',
        'test_true_divide_float',
        'test_true_divide_frozenset',
        'test_true_divide_int',
        'test_true_divide_list',
        'test_true_divide_None',
        'test_true_divide_NotImplemented',
        'test_true_divide_range',
        'test_true_divide_set',
        'test_true_divide_slice',
        'test_true_divide_str',
        'test_true_divide_tuple',

        'test_xor_bool',
        'test_xor_bytearray',
        'test_xor_bytes',
        'test_xor_class',
        'test_xor_complex',
        'test_xor_dict',
        'test_xor_float',
        'test_xor_frozenset',
        'test_xor_int',
        'test_xor_list',
        'test_xor_None',
        'test_xor_NotImplemented',
        'test_xor_range',
        'test_xor_set',
        'test_xor_slice',
        'test_xor_str',
        'test_xor_tuple',
    ]


class InplaceFrozensetOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'frozenset'

    not_implemented = [
        'test_add_bool',
        'test_add_bytearray',
        'test_add_bytes',
        'test_add_class',
        'test_add_complex',
        'test_add_dict',
        'test_add_float',
        'test_add_frozenset',
        'test_add_int',
        'test_add_list',
        'test_add_None',
        'test_add_NotImplemented',
        'test_add_range',
        'test_add_set',
        'test_add_slice',
        'test_add_str',
        'test_add_tuple',

        'test_and_bool',
        'test_and_bytearray',
        'test_and_bytes',
        'test_and_class',
        'test_and_complex',
        'test_and_dict',
        'test_and_float',
        'test_and_frozenset',
        'test_and_int',
        'test_and_list',
        'test_and_None',
        'test_and_NotImplemented',
        'test_and_range',
        'test_and_set',
        'test_and_slice',
        'test_and_str',
        'test_and_tuple',

        'test_floor_divide_bool',
        'test_floor_divide_bytearray',
        'test_floor_divide_bytes',
        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_dict',
        'test_floor_divide_float',
        'test_floor_divide_frozenset',
        'test_floor_divide_int',
        'test_floor_divide_list',
        'test_floor_divide_None',
        'test_floor_divide_NotImplemented',
        'test_floor_divide_range',
        'test_floor_divide_set',
        'test_floor_divide_slice',
        'test_floor_divide_str',
        'test_floor_divide_tuple',

        'test_lshift_bool',
        'test_lshift_bytearray',
        'test_lshift_bytes',
        'test_lshift_class',
        'test_lshift_complex',
        'test_lshift_dict',
        'test_lshift_float',
        'test_lshift_frozenset',
        'test_lshift_int',
        'test_lshift_list',
        'test_lshift_None',
        'test_lshift_NotImplemented',
        'test_lshift_range',
        'test_lshift_set',
        'test_lshift_slice',
        'test_lshift_str',
        'test_lshift_tuple',

        'test_modulo_bool',
        'test_modulo_bytearray',
        'test_modulo_bytes',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_range',
        'test_modulo_set',
        'test_modulo_slice',
        'test_modulo_str',
        'test_modulo_tuple',

        'test_multiply_bool',
        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_dict',
        'test_multiply_float',
        'test_multiply_frozenset',
        'test_multiply_int',
        'test_multiply_list',
        'test_multiply_None',
        'test_multiply_NotImplemented',
        'test_multiply_range',
        'test_multiply_set',
        'test_multiply_slice',
        'test_multiply_str',
        'test_multiply_tuple',

        'test_or_bool',
        'test_or_bytearray',
        'test_or_bytes',
        'test_or_class',
        'test_or_complex',
        'test_or_dict',
        'test_or_float',
        'test_or_frozenset',
        'test_or_int',
        'test_or_list',
        'test_or_None',
        'test_or_NotImplemented',
        'test_or_range',
        'test_or_set',
        'test_or_slice',
        'test_or_str',
        'test_or_tuple',

        'test_power_bool',
        'test_power_bytearray',
        'test_power_bytes',
        'test_power_class',
        'test_power_complex',
        'test_power_dict',
        'test_power_float',
        'test_power_frozenset',
        'test_power_int',
        'test_power_list',
        'test_power_None',
        'test_power_NotImplemented',
        'test_power_range',
        'test_power_set',
        'test_power_slice',
        'test_power_str',
        'test_power_tuple',

        'test_rshift_bool',
        'test_rshift_bytearray',
        'test_rshift_bytes',
        'test_rshift_class',
        'test_rshift_complex',
        'test_rshift_dict',
        'test_rshift_float',
        'test_rshift_frozenset',
        'test_rshift_int',
        'test_rshift_list',
        'test_rshift_None',
        'test_rshift_NotImplemented',
        'test_rshift_range',
        'test_rshift_set',
        'test_rshift_slice',
        'test_rshift_str',
        'test_rshift_tuple',

        'test_subtract_bool',
        'test_subtract_bytearray',
        'test_subtract_bytes',
        'test_subtract_class',
        'test_subtract_complex',
        'test_subtract_dict',
        'test_subtract_float',
        'test_subtract_frozenset',
        'test_subtract_int',
        'test_subtract_list',
        'test_subtract_None',
        'test_subtract_NotImplemented',
        'test_subtract_range',
        'test_subtract_set',
        'test_subtract_slice',
        'test_subtract_str',
        'test_subtract_tuple',

        'test_true_divide_bool',
        'test_true_divide_bytearray',
        'test_true_divide_bytes',
        'test_true_divide_class',
        'test_true_divide_complex',
        'test_true_divide_dict',
        'test_true_divide_float',
        'test_true_divide_frozenset',
        'test_true_divide_int',
        'test_true_divide_list',
        'test_true_divide_None',
        'test_true_divide_NotImplemented',
        'test_true_divide_range',
        'test_true_divide_set',
        'test_true_divide_slice',
        'test_true_divide_str',
        'test_true_divide_tuple',

        'test_xor_bool',
        'test_xor_bytearray',
        'test_xor_bytes',
        'test_xor_class',
        'test_xor_complex',
        'test_xor_dict',
        'test_xor_float',
        'test_xor_frozenset',
        'test_xor_int',
        'test_xor_list',
        'test_xor_None',
        'test_xor_NotImplemented',
        'test_xor_range',
        'test_xor_set',
        'test_xor_slice',
        'test_xor_str',
        'test_xor_tuple',
    ]
