_init__(self, num_heads,head_size):
    #     super().__init__()
    #     self.head = nn.ModuleList([Head(head_size) for _ in range(num_heads)])
    #     self.proj = nn.Linear(head_size*n_embd,n_embd)
    #     self.dropout = nn.Dropout(dropout)
    # def forward(self,x):
    #     out = torch.cat([h(x) for h in self.head],dim=-1)
    #     out = self.dropout(self.proj(out))
    #     return out