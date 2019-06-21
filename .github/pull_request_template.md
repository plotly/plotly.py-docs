Doc upgrade checklist:

- [ ] old boilerplate at top and bottom of file has been removed
- [ ] Every example is independently runnable and is optimized for short line count
- [ ] no more `plot()` or `iplot()`
- [ ] `graph_objs` has been renamed to `graph_objects`
- [ ] `fig = <something>` call is high up in each example
- [ ] minimal creation of intermediate `trace` objects
- [ ] liberal use of `add_trace` and `update_layout`
- [ ] `fig.show()` at the end of each example
- [ ] `px` example at the top if appropriate
- [ ] `v4upgrade: true` metadata added
- [ ] minimize usage of hex codes for colors in favour of those in https://github.com/plotly/plotly.py-docs/issues/14
