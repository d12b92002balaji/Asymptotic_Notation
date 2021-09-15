#void nFacRuntimeFunc(int n) {
#  for(int i=0; i<n; i++) {
#    nFacRuntimeFunc(n-1);
  #}
#}

def facRumTime(n):
    for i in range(n):
        facRumTime(n-1)
fact=facRumTime(5)
print(fact)