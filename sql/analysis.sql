SELECT
  channel,
  COUNT(*) AS visitors,
  SUM(signed_up) AS signups,
  SUM(activated) AS activated_users,
  SUM(converted) AS conversions,
  1.0 * SUM(converted) / COUNT(*) AS conversion_rate
FROM funnel_events
GROUP BY channel
ORDER BY conversion_rate DESC;

SELECT
  variant,
  COUNT(*) AS users,
  SUM(converted) AS conversions,
  1.0 * SUM(converted) / COUNT(*) AS conversion_rate
FROM funnel_events
GROUP BY variant;
