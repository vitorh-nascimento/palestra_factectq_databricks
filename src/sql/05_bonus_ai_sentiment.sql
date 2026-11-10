-- Bônus: Classificação de Sentimento com GenAI nativa (AI Functions)
SELECT 
    review, 
    ai_analyze_sentiment(review) AS sentimento 
FROM samples.bakehouse.media_customer_reviews 
LIMIT 10;

