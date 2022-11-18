#!/bin/bash
# curl -X GET https://api.github.com/repos/datamove/practice-repo/issues
curl -H "Accept: application/vnd.github.v3+json" 'https://api.github.com/repos/datamove/linux-git2/pulls?state=all&per_page=100' | jq "map(select(.user."login"==\"$1\"))" >> /tmp/airat_tmp
# $tmp1 | jq "map(select(.user."login"==\"$1\"))" >> /tmp/airat_tmp
for (( i=2; i <= 4; i++ ))
do
curl -H "Accept: application/vnd.github.v3+json" "https://api.github.com/repos/datamove/linux-git2/pulls?state=all&per_page=100&page=$i" | jq "map(select(.user."login"==\"$1\"))">>/tmp/airat_tmp
# $tmp2 | jq "map(select(.user."login"==\"$1\"))" >> /tmp/airat_tmp
done
# $tmp1 | jq "map(select(.user."login"==\"$1\"))" >> /tmp/airat_tmp
counter=$(cat /tmp/airat_tmp | jq '.[].number' | wc -l)
echo "PULLS $counter"
first=$(cat /tmp/airat_tmp | jq '.[].number' | sort | head -1)
echo "EARLIEST $first"
mer=$(cat /tmp/airat_tmp | jq '.[].merged_at' | head -1)
if [[ $mer -eq "null" ]]; then
echo "MERGED 0"
else
  echo "MERGED 1"
fi 
