#!/bin/sh
rm NAR_gen
rm -f src/RuleTable.c
set -e
Str=`ls src/*.c src/NetworkNAR/*.c | xargs`
echo $Str
echo "Compilation started:"
BaseFlags="-mfpmath=sse -msse2 -pthread -lpthread -D_POSIX_C_SOURCE=199506L -pedantic -std=c99 -g3 -O3 $Str -lm -oNAR_gen"

gcc -DSTAGE=1 -Wall -Wextra -Wformat-security $BaseFlags
echo "First stage done, generating RuleTable.c now, and finishing compilation."
./NAR_gen NAL_GenerateRuleTable > ./src/RuleTable.c


