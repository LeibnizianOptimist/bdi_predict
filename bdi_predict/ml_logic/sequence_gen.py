import numpy as np
import random

class WindowGenerator():
  def __init__(self, input_width, label_width, shift,
               train_df, val_df, test_df,
               label_columns=None):
    # Store the raw data.
    self.train_df = train_df
    self.val_df = val_df
    self.test_df = test_df

    # Work out the label column indices.
    self.label_columns = label_columns
    if label_columns is not None:
      self.label_columns_indices = {name: i for i, name in
                                    enumerate(label_columns)}
    self.column_indices = {name: i for i, name in
                           enumerate(train_df.columns)}

    # Work out the window parameters.
    self.input_width = input_width
    self.label_width = label_width
    self.shift = shift

    self.total_window_size = input_width + shift

    self.input_slice = slice(0, input_width)
    self.input_indices = np.arange(self.total_window_size)[self.input_slice]

    self.label_start = self.total_window_size - self.label_width
    self.labels_slice = slice(self.label_start, None)
    self.label_indices = np.arange(self.total_window_size)[self.labels_slice]

  def __repr__(self):
    return '\n'.join([
        f'Total window size: {self.total_window_size}',
        f'Input indices: {self.input_indices}',
        f'Label indices: {self.label_indices}',
        f'Label column name(s): {self.label_columns}'])

class Sequential:

    def __init__(self, data):
        self.data = data

    def sequence_data(self, sequence, target):
        data = self.data.copy()
        shift_data = data.shift(5)
        target_data = shift_data[target]

        feature_data = data.drop(target, axis=1)
        target_data = target_data[sequence:]
        datas = data
        data_windows = list()

        num = sequence
        for num in range(len(target_data)):
            if num + sequence >= len(target_data):
                break
            window_scale_features = datas[num: num+sequence].drop(target, axis=1)
            window = {"target": target_data[num + sequence], "features": window_scale_features}
            data_windows.append(window)
            num = num + 1

        return data_windows

    def randomize_window(self, window_data):
        random_windows = random.sample(window_data, len(window_data))
        return random_windows

    def reorganaize_sequence_data(self, train, test):
        train_window_feature = []
        train_window_target = []

        test_window_feature = []
        test_window_target = []

        num = 0
        for window in train:
            train_window_feature.append(train[num]["features"])
            train_window_target.append([train[num]["target"]])
            num = num + 1

        num = 0
        for window in test:
            test_window_feature.append(test[num]["features"])
            test_window_target.append([test[num]["target"]])
            num = num + 1

        train_window_feature = np.array(np.array(train_window_feature))
        train_window_target = np.array(train_window_target)

        test_window_feature = np.array(np.array(test_window_feature))
        test_window_target = np.array(test_window_target)

        organaized_data = {"train":[train_window_feature, train_window_target], "test":[test_window_feature, test_window_target]}

        return organaized_data
