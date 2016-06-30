

CREATE CONSTRAINT ON (member:Member) ASSERT member.member_id IS UNIQUE

USING PERIODIC COMMIT
LOAD CSV FROM "file:///common_connection_200k.csv" AS row
MERGE (:Member {member_id: row[0]});

USING PERIODIC COMMIT
LOAD CSV FROM "file:///common_connection_200k.csv" AS row
MATCH (member:Member {member_id: row[0]})
MATCH (m2:Member {member_id: row[1]})
MERGE (member)-[:CONNECTED_TO]-(m2)

MATCH (a:Member)-[r:CONNECTED_TO]->(:Member)<-[:CONNECTED_TO]-(b:Member)
    WHERE NOT a=b
WITH a, b, count(r) AS commonConnectionCount
RETURN a.member_id, b.member_id, commonConnectionCount ORDER BY commonConnectionCount DESC