
def func_gen():
    for _ in [34, 234, 102]:
        yield _

gen_iterator = func_gen().__iter__()
for _ in range (1, 4):
    print(gen_iterator.__next__())

print(type(gen_iterator))
print(iter([34, 234, 102]))
