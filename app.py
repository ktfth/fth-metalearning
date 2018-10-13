import os
import tensorflow as tf

def fetch_brand_data(brand=None):
    try:
        if not os._exists('fth.png'):
            brand = tf.keras.utils.get_file('fth.png', 'https://fth.sh/img/fth.png')
            print("Expecting the metalearning process based on the pointeneed extraction...")
    except Exception as e:
        tf.logging.info(e)
    finally:
        print('Download aggain!')
        return brand

def main(unusued_argv):
    fetch_brand_data()

if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
