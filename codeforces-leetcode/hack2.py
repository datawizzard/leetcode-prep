import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
cache[36][36]
def dp(a, n,sum,taken):
{
	if (n == 0):
		return max((a[0] + sum) % m, (sum % m))
	int &ans = cache[n - 1][taken];
	if (ans != -1)return ans;

	else
	{
		ans = max(dp(a, n - 1, (a[n] + sum) % m, ++taken), dp(a, n - 1, sum % m, taken));
		return ans;
	}
}
int32_t main()
{
	int n;
	cin >> n >> m;
	int a[n];
	memset(cache, -1, sizeof(cache));
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}
	int ans = 0;
	ans = dp(a, n - 1, 0, 0);
	cout << ans << endl;

	return 0;
}