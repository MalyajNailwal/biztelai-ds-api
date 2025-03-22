import matplotlib.pyplot as plt
import seaborn as sns

def plot_agent_distribution(df):
    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x='agent')
    plt.title("Agent Message Count")
    plt.tight_layout()
    plt.savefig("agent_message_distribution.png")

def plot_sentiment_distribution(df):
    plt.figure(figsize=(8,5))
    sns.countplot(data=df, x='sentiment', hue='agent')
    plt.title("Sentiment Distribution by Agent")
    plt.tight_layout()
    plt.savefig("sentiment_distribution.png")

def summarize_conversation(df, conv_id):
    subset = df[df['conversation_id'] == conv_id]
    summary = {
        "article_url": subset['article_url'].iloc[0],
        "agent_1_msgs": subset[subset['agent'] == 'agent_1'].shape[0],
        "agent_2_msgs": subset[subset['agent'] == 'agent_2'].shape[0],
        "agent_1_sentiment": subset[subset['agent'] == 'agent_1']['sentiment'].mode()[0],
        "agent_2_sentiment": subset[subset['agent'] == 'agent_2']['sentiment'].mode()[0],
    }
    return summary