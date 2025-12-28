from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel # With this we can run multiple chains parallely
from dotenv import load_dotenv
import os

load_dotenv()

model1 = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
)

model2 = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("NEW_GROQ_API_KEY"),
    temperature=0,
)

prompt1 = PromptTemplate(
    template="Generate short and Simple Notes from the following text \n {text}",
    input_variables=['text']
)
prompt2 = PromptTemplate(
    template="Generate 5 Short Questions and answer from the following text \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="Merge the provided Notes and Quiz into a Single Document \n Notes -> {notes} and Quiz -> {quiz}",
    input_variables=['notes','quiz']

)


parser = StrOutputParser()

# RunnableParallel is used to run chain parallely
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser ,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

# Koi se bhi model ke pass bhej skte ho.

chain = parallel_chain | merge_chain

text = '''
Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression. Its core objective is geometric: find a decision boundary that maximizes separation between classes. This boundary is called a hyperplane. In two dimensions, it is a line. In higher dimensions, it is a plane or hypersurface.

SVM does not aim to minimize classification error directly. It maximizes the margin. The margin is the distance between the hyperplane and the closest data points from each class. These closest points are called support vectors. Only support vectors influence the final model. All other points are irrelevant once the margin is fixed.

Mathematically, SVM solves a constrained optimization problem. It minimizes the norm of the weight vector while enforcing class separation constraints. This converts learning into a convex quadratic optimization problem with a guaranteed global optimum. No local minima. Deterministic outcome.

For linearly separable data, SVM constructs a hard-margin classifier. This assumes perfect separation. Real data violates this assumption. Soft-margin SVM introduces slack variables to allow misclassification. A regularization parameter C controls the trade-off between margin width and classification error. Large C prioritizes correct classification. Small C prioritizes a wider margin.

Nonlinear data requires transformation. SVM handles this through the kernel trick. Instead of explicitly mapping data into a higher-dimensional space, SVM uses kernel functions to compute inner products implicitly. Common kernels include linear, polynomial, radial basis function (RBF), and sigmoid. Kernel choice defines the geometry of the decision boundary.

RBF kernel is the default in practice. It creates flexible, localized decision regions. It introduces a gamma parameter controlling influence radius of support vectors. High gamma leads to overfitting. Low gamma leads to underfitting. Polynomial kernels model interactions of features. Linear kernels scale best for high-dimensional sparse data.

SVM regression is called Support Vector Regression (SVR). It uses an epsilon-insensitive loss function. Errors within an epsilon tube around the prediction are ignored. Only points outside the tube become support vectors. The objective remains margin maximization under tolerance constraints.

SVM is effective in high-dimensional spaces. It handles small-to-medium datasets well. It is robust to overfitting when properly regularized. It performs poorly on extremely large datasets due to quadratic or cubic training complexity. Kernel SVMs do not scale well without approximation methods.

Feature scaling is mandatory. Unscaled features distort distance calculations and margins. SVM is sensitive to noise when C is large. Model interpretability is low for nonlinear kernels. Hyperparameter tuning is critical and non-optional.

SVM represents learning as geometry, optimization, and constraints rather than probability estimation. It enforces structure, not likelihood. It trades flexibility for theoretical guarantees and margin-based generalization.

'''

result = chain.invoke({"text":text})

print(result)
chain.get_graph().print_ascii()