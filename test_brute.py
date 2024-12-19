import pytest
from brute import Brute
def describe_Brute():
    @pytest.fixture
    def cracker():
        return Brute("TDD")
    def describe_bruteOnce():
        def it_passes_once_with_empty_string():
            b = Brute('')
            return_value = b.bruteOnce('')
            assert return_value
            assert b.target == 'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'
            assert b.target != ''
        def it_passes_once_with_string_e_of_size_one():
            b = Brute('e')
            return_value = b.bruteOnce('e')
            assert return_value
            assert b.target == '87c568e037a5fa50b1bc911e8ee19a77c4dd3c22bce9932f86fdd8a216afe1681c89737fada6859e91047eece711ec16da62d6ccb9fd0de2c51f132347350d8c'
            assert b.target != 'e'
        def it_passes_once_with_string_TDD_of_size_three(cracker):
            return_value = cracker.bruteOnce('TDD')
            assert return_value
            assert cracker.target == '00ab3eef51b8551de98a6cab9352898aed783a35995285659bbdd40162fda9505aebff62d7bf29fd7474d45f303f3cddd8d3aa0383f45a9f9facd6a8860f7938'
            assert cracker.target != 'TDD'
    def describe_bruteMany():
        def it_passes_many_with_empty_string(mocker):
            mock_randomGuess = mocker.patch.object(Brute, 'randomGuess', return_value='')
            mock_hash = mocker.patch.object(Brute, 'hash', return_value='cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e')
            b = Brute('')
            result = b.bruteMany()
            mock_hash.assert_called()
            mock_randomGuess.assert_called()
            assert result != -1
            assert result > 0
        def it_passes_many_with_string_e_of_size_one(mocker):
            mock_randomGuess = mocker.patch.object(Brute, 'randomGuess', return_value='e')
            mock_hash = mocker.patch.object(Brute, 'hash', return_value='87c568e037a5fa50b1bc911e8ee19a77c4dd3c22bce9932f86fdd8a216afe1681c89737fada6859e91047eece711ec16da62d6ccb9fd0de2c51f132347350d8c')
            b = Brute('e')
            result = b.bruteMany()
            mock_hash.assert_called()
            mock_randomGuess.assert_called()
            assert result != -1
            assert result > 0
        def it_passes_many_with_string_TDD_of_size_three(mocker, cracker):
            mock_randomGuess = mocker.patch.object(Brute, 'randomGuess', return_value='TDD')
            mock_hash = mocker.patch.object(Brute, 'hash', return_value='00ab3eef51b8551de98a6cab9352898aed783a35995285659bbdd40162fda9505aebff62d7bf29fd7474d45f303f3cddd8d3aa0383f45a9f9facd6a8860f7938')
            result = cracker.bruteMany()
            mock_hash.assert_called()
            mock_randomGuess.assert_called()
            assert result != -1
            assert result > 0