<script lang="ts">
	import type { TypographyProps } from '$components/typography';
	import { cn } from '$utils';

	let { children, class: className, ...props }: TypographyProps = $props();
</script>

<h2
	class={cn(
		'scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0',
		className,
	)}
	{...props}
>
	{@render children?.()}
</h2>
