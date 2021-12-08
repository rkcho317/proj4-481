import nn

class PerceptronModel(object):
    def __init__(self, dimensions):
        """
        Initialize a new Perceptron instance.

        A perceptron classifies data points as either belonging to a particular
        class (+1) or not (-1). `dimensions` is the dimensionality of the data.
        For example, dimensions=2 would mean that the perceptron must classify
        2D points.
        """
        self.w = nn.Parameter(1, dimensions)

    def get_weights(self):
        """
        Return a Parameter instance with the current weights of the perceptron.
        """
        return self.w

    def run(self, x):
        """
        Calculates the score assigned by the perceptron to a data point x.

        Inputs:
            x: a node with shape (1 x dimensions)
        Returns: a node containing a single number (the score)
        """
        "*** YOUR CODE HERE ***"

# =============================================================================
#         Implement the run(self, x) method. 
#         This should compute the dot product of the stored weight vector and the given input,
#         returning an nn.DotProduct object.
# =============================================================================
        
        #output = nn.DotProduct(self.get_weights(), x)
        #print(output)
        return nn.DotProduct(self.get_weights(), x)

    def get_prediction(self, x):
        """
        Calculates the predicted class for a single data point `x`.

        Returns: 1 or -1
        """
        "*** YOUR CODE HERE ***"
        
# =============================================================================
#         Implement get_prediction(self, x), 
#         which should return 1 if the dot product is non-negative or −1 otherwise.
#         You should use nn.as_scalar to convert a scalar Node into a Python floating-point number.
# =============================================================================
        
        #this would run if the input were not already a single-item node
        output = self.run(x)
        #print(output)
        output = nn.as_scalar(output)
        #print(output)
        if output < 0.0:
            return -1.0
        else:
            return 1.0

    def train(self, dataset):
        """
        Train the perceptron until convergence.
        """
        "*** YOUR CODE HERE ***"
        
# =============================================================================
#         Write the train(self) method. 
#         This should repeatedly loop over the data set and 
#         make updates on examples that are misclassified. 
#         Use the update method of the nn.Parameter class to update the weights. 
#         When an entire pass over the data set is completed without making any mistakes,
#         100% training accuracy has been achieved, and training can terminate.
# =============================================================================

        weight_set = self.get_weights()
        learning_rate = 0.2
        """print("weights")
        print(weight_set)
        print(weight_set.data)
        print(weight_set.data[0])
        for item in weight_set.data[0]:
            print(item)
        
        print("dataset")"""
        
        batch_size = 1
        """for x,y in dataset.iterate_once(batch_size):
            print(x)
            print(x.data)
            for item in x.data[0]:
                print(item)
            print(y)
            print(y.data)
            break"""
        
        """print("dot product")
        delW = nn.DotProduct(weight_set, x)
        print(delW)
        print(delW.data)"""
        
        print("iterate thru dataset")
        
        #if t=a, do nothing
            #else error, adjust weight vector for next case by 
            #   w^n+1 = w^n + delta w^n
            #weight adjustment, or delta w^n can be defined:
            #   delta w^n = l (t - a) x sub i
            #       where l is the learning rate between 0 and 1 controlling speed of convergence
            #       t is the desired output value (class label) from the training set
            #       a is the perceptron output value (either +/-1) for
            #       x sub i, the current input case
        
        #completed a full loop without any errors
        notConverged = True
        while (notConverged):
            notConverged = True
            mismatches = False
            print("top of loop")
            print("mismatch!", mismatches)
            print("notConverged!", notConverged)
            # iterate through dataset once
            for x,y in dataset.iterate_once(batch_size):
                print("dataset loop", x, y)
                #the net is the sum of (each weight * matching data point)
                """effNet = 0"""
                #for each pair in weight_sprint(effNet)et and x.data
                """for index in range( len(x.data[0]) ):
                    #multiply each weight by matching data point, add to net
                    effNet += weight_set.data[0][index] * x.data[0][index]
                    print(effNet)
                    print(nn.DotProduct(weight_set, x))
                    print(nn.as_scalar(nn.DotProduct(weight_set, x)))"""
                #now that you have the net of the data,
                #   check to see if predicted value matches the dataset's target
                #   if it matches, no problem - if mismatch, need delta w
                """if effNet < 0.0:
                    predict = -1.0
                else:
                    predict = 1.0"""
                #effNet = nn.DotProduct(weight_set, x)
                #print(effNet)
                #print(nn.as_scalar(effNet))
                effNet = self.run(x)
                #print(effNet)
                #print(nn.as_scalar(effNet))
                #if y.data[0][0] != self.get_prediction(nn.DataNode(effNet)):
                if nn.as_scalar(y) != self.get_prediction(x):
                    #how do you get delta w?
                    print("mismatch!", mismatches)
                    print("f(net) is ", effNet, " which is ", nn.as_scalar(effNet))
                    print("x from training data is ", x, " which is ", x.data)
                    print(x, " has predicted output of ", self.get_prediction(x))
                    print("y from training data is ", y, " which is ", nn.as_scalar(y))
                    #now that we actually have shit figured, we change weights now
                    #deltaW = learning rate * (target - prediction) * current input case
                    print("before weights: ", self.get_weights())
                    print("before weights data: ", self.get_weights().data)
                    deltaW = learning_rate * (nn.as_scalar(y) - self.get_prediction(x))
                    print("delta w: ", deltaW)
                    nn.Parameter.update(self.get_weights(), x, deltaW)
                    print("after weights: ", self.get_weights())
                    print("after weights data: ", self.get_weights().data)
                    #weight_set = self.get_weights()
                    mismatches = True
                    print("mismatch!", mismatches)
                #else:
                    #print("match! do nothing!")
            print("end of loop")
            print("mismatch!", mismatches)
            print("notConverged!", notConverged)
            if mismatches == False:
                notConverged = False
                print("notConverged!", notConverged)
            

class RegressionModel(object):
    """
    A neural network model for approximating a function that maps from real
    numbers to real numbers. The network should be sufficiently large to be able
    to approximate sin(x) on the interval [-2pi, 2pi] to reasonable precision.
    """
    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
        Returns:
            A node with shape (batch_size x 1) containing predicted y-values
        """
        "*** YOUR CODE HERE ***"

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
            y: a node with shape (batch_size x 1), containing the true y-values
                to be used for training
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"

class DigitClassificationModel(object):
    """
    A model for handwritten digit classification using the MNIST dataset.

    Each handwritten digit is a 28x28 pixel grayscale image, which is flattened
    into a 784-dimensional vector for the purposes of this model. Each entry in
    the vector is a floating point number between 0 and 1.

    The goal is to sort each digit into one of 10 classes (number 0 through 9).

    (See RegressionModel for more information about the APIs of different
    methods here. We recommend that you implement the RegressionModel before
    working on this part of the project.)
    """
    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Your model should predict a node with shape (batch_size x 10),
        containing scores. Higher scores correspond to greater probability of
        the image belonging to a particular class.

        Inputs:
            x: a node with shape (batch_size x 784)
        Output:
            A node with shape (batch_size x 10) containing predicted scores
                (also called logits)
        """
        "*** YOUR CODE HERE ***"

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        The correct labels `y` are represented as a node with shape
        (batch_size x 10). Each row is a one-hot vector encoding the correct
        digit class (0-9).

        Inputs:
            x: a node with shape (batch_size x 784)
            y: a node with shape (batch_size x 10)
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"

class LanguageIDModel(object):
    """
    A model for language identification at a single-word granularity.

    (See RegressionModel for more information about the APIs of different
    methods here. We recommend that you implement the RegressionModel before
    working on this part of the project.)
    """
    def __init__(self):
        # Our dataset contains words from five different languages, and the
        # combined alphabets of the five languages contain a total of 47 unique
        # characters.
        # You can refer to self.num_chars or len(self.languages) in your code
        self.num_chars = 47
        self.languages = ["English", "Spanish", "Finnish", "Dutch", "Polish"]

        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"

    def run(self, xs):
        """
        Runs the model for a batch of examples.

        Although words have different lengths, our data processing guarantees
        that within a single batch, all words will be of the same length (L).

        Here `xs` will be a list of length L. Each element of `xs` will be a
        node with shape (batch_size x self.num_chars), where every row in the
        array is a one-hot vector encoding of a character. For example, if we
        have a batch of 8 three-letter words where the last word is "cat", then
        xs[1] will be a node that contains a 1 at position (7, 0). Here the
        index 7 reflects the fact that "cat" is the last word in the batch, and
        the index 0 reflects the fact that the letter "a" is the inital (0th)
        letter of our combined alphabet for this task.

        Your model should use a Recurrent Neural Network to summarize the list
        `xs` into a single node of shape (batch_size x hidden_size), for your
        choice of hidden_size. It should then calculate a node of shape
        (batch_size x 5) containing scores, where higher scores correspond to
        greater probability of the word originating from a particular language.

        Inputs:
            xs: a list with L elements (one per character), where each element
                is a node with shape (batch_size x self.num_chars)
        Returns:
            A node with shape (batch_size x 5) containing predicted scores
                (also called logits)
        """
        "*** YOUR CODE HERE ***"

    def get_loss(self, xs, y):
        """
        Computes the loss for a batch of examples.

        The correct labels `y` are represented as a node with shape
        (batch_size x 5). Each row is a one-hot vector encoding the correct
        language.

        Inputs:
            xs: a list with L elements (one per character), where each element
                is a node with shape (batch_size x self.num_chars)
            y: a node with shape (batch_size x 5)
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
