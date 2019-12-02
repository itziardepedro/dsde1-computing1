'''
test-tfidf_corpus.py

Test file for TFIDFCorpus class of TF-IDF exercise.
'''

import unittest
import tfidf_corpus as tf


class TestTF(unittest.TestCase):
    def set_up(self):
        pass

    def test_files(self):
        '''Test reading in the list of filenames'''
        my_tfidf = tf.TFIDFCorpus('text-files')
        result = my_tfidf.get_filenames()
        file_list = ['a-drinking-song-yeats.txt',
                     'christmas-carol.txt',
                     'mercutio.txt', 
                     'the-start-teasdale.txt']
        self.assertEqual(result, file_list)

    
    def test_create_docs(self):
        '''Test creation of TFDocument instances'''
        my_tfidf = tf.TFIDFCorpus('text-files')

        result = len(my_tfidf.docs)
        self.assertEqual(result, 4)
    
    def test_computeidf(self):
        '''Test generation of IDF dictionary'''
        my_tfidf = tf.TFIDFCorpus('text-files')
        k = my_tfidf.idf.keys()
        self.assertEqual(my_tfidf.idf['light'], 2.0)
        self.assertEqual(my_tfidf.idf['cold'], 2.0)
        self.assertEqual(my_tfidf.idf['time'], 2.0)
        self.assertNotIn('facebook', k)


if __name__=='__main__':
    unittest.main()
